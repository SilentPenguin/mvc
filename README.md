mvc
===

a simple mvc implementation written in and for python3.4

bugs? this is likely to be rife with them. There's doubtlessly performance issues which need ironing out and encoding
issues. The wsgi interface implementation is rudementory at best.

This module currently has a couple of main aspects, templating, routing and modelbinding

Changes will come later in the form of model binding, configuration and better module structuring

Templating
==========
This is both the module's star of the show, and it's downfall. The templating structure is very similar to python itself.

The advantage of this is that it's very short code, because it directly uses compile(). The disadvantage is that the implementation is especially ugly to look at and the template code is whitespace varient, because python itself is.

So, how does that all work? Simply, the templating engine encounters a line in your template and decides if it should be converted to str, expression or raw text, in that order. So if you're expecting a line to be python or an inserted string, and it's not, it's likely because there's a syntax error on that particular line.

That sounds disgusting, "why has this horror been created?" I hear you cry. Simple, so that this is a valid template:

    # Example.pyhtml
    <html>
        <head>
            <title> some title
        <body>
            if model.value is not None:
                <div>
                    model.value
            else:
                <div> nothing?

It has taken me a couple of hours to get used to looking at templates without weird characters like @, %, $ or {}.
The implicitly closed html tags hasn't helped that.

This does have one repercussion, once a line is interpreted as something, part of the line can't be interpreted as something else, so to insert a model value into a body of text that statement needs to appear on a seperate line. After using the template language for a bit, this isn't as bad as it sounds, as it forces you to keep anything you're assigning/printing seperate, but I will likely be modifying this so that lines at the same level without a blank line or html tag between them are compressed into one line.

Rendering Templates
-------------------

There are several ways you can render templates. the easiest way being to use the Controller class, and using its

    view(self, model, "./path/to/template.pyhtml")

method, passing your template and view model as a parameter, this method will then ensure your template is compiled (if it needs compiling) and it's output is placed in a response.

you can seperate out mvc.templating.template.py entirely though since it has no dependancies on other parts of the system and use

    TemplateEngine("./path/to/template.pyhtml")
    html = template(model)
    
to compile and output the raw html.

Routing
=======

Currently, mvc uses a base Route() object stored in mvc.routing.route.route_map. This should change in the future to better structure the system.

Routes themselves refer to a callable, or a child routes, and a regex string to match incoming urls.

When you add a url to the application's route_map, it's broken up into its component parts and stored as a tree.

There are then several ways you can apply your routes, detailed below.

note, routes always start with a /, and the ^ and $ in the regex routes are automatically applied when resolving the
route_map, only named parameters are currently supported by routes.

Decorators
----------

flask-esque routes can be created by adding named parameters as arguments

    @route('/my/url/(?P<id>[0-9]{2})')
    def my_action(self, id):
        pass

Route_map Appending
-------------------

you can also work with the routes directly using django-esque routing

    route_map += Route('/my/url/(?P<id>[0-9]{2})', my_action)

It's worth adding, that my_action could easily be another Route(), or you could store a route you create and call += on
it as well and the routemap would have the routes you've passed added too them at the point you have added them. So this:

    my_route = Route('/my/base', base_action) #reachable via /my/base
    my_route += Route('/child', child_action) #reachable via /my/base/child
    route_map += my_route
    
produces the same result as:
    
    route_map += Route('/my/base', base_action)
    route_map += Route('/my/base/child', child_action)
    
both functionally and performance wise, so just use routes however it suits you best.

With either decorators or directly editing the route_map, as long as your code is hit, either by an import, function call,
or keeping your entire site in one file, the routing will work with either method, interchangably.

example
-------

Check out https://github.com/SilentPenguin/mvc-example for a working example using route_map appending.

Model Binding
=============

Modelbinding is still in it's infancy, however it has a simple to use interface. There are two main classes in modelbinding, Model, and Field.

Field
-----
Field provides a placeholder for your properties. It's structure is as so:

    __init__(self, default = None, validate = None, minimum = 0, maximum = 1):

* default - default value for the field, if nothing is assigned to the field, this will be the value it will return.
* validate - either a regex string or callable, creating a regex or callable validator respectively. For a callable validator, the first argument will one of the values being assigned, and the validator must return boolean to decide if the value given is valid.
* minimum - the minimum number of field values for this field in order for the field to be valid. Setting the minimum to a number greater than 0 will make the field required, meaning it will not validate if it does not have a value.
* maximum - the maximum number of field values for this field.

properties:

* value - returns the value, always be stored internally as a list, but if the maximum number of values on a field is defined as 1, it's .value will return it's value type, otherwise it will return a list. validate can also be assigned to.
* _value - the actual value of the field, fetch this if you always want to work in lists.
* valid - is true if value is valid, validate will iterate over each item in _value, validating the values, if one value is not valid, this will be false.


Model
-----
Model is used to subclass your model classes, providing the nessicary functionality to result in modelbinding magic. It abstracts the dictionaryness of request forms, and providing default values and validation in it's place.

Below is an example Model class:

    class MyModel(Model):
        my_field = Field(validate = '^\w+$')
        second_field = Field(validate = lambda v: bool(v))
        
similarly to Field, Model has a valid property which returns True or False if the fields (and models) inside your model are invalid.


You'll probably be able to see that this model, named MyModel, has two Fields named my_field and second_field. More specifically, my_field only allows word characters, while second_field checks for non-false values. Obviously this is just a basic example to get the brain gears going.

It's constructor takes a request, so you can pass the request context into the model and the model will be automatically populated for you. Once you've defined your model, you will want to use it, which you'd do simply by calling

    model = MyModel(request)