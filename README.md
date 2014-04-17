mvc
===

a simple mvc implementation

bugs? this is likely to be rife with them. There's doubtlessly performance issues which need ironing out and encoding
issues. The wsgi interface implementation is rudementory at best.

This module currently has two main aspects, templating, and routing

Changes will come later in the form of model binding, configuration and better module structuring

Templating
==========
This is both the module's star of the show, and it's downfall. The templating structure is very similar to python itself.
The advantage of this is that it's very short code, because it directly uses compile(). The disadvantage is that it is 
both especially ugly to look at and is whitespace varient, because python itself is.

So, how does it work, simply, the templating engine encounters a line in your template and decides if it should be
converted to str, expression or raw text, in that order.

That sounds disgusting, "why has this horror been created?" I hear you cry.
Simple, so that this is valid template:

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

It has taken me a couple of hours to get used to looking at templates without weird characters like @, %, $ or {}, and
implicitly closing html tags hasn't helped that.

This does have one repercussion, anything interpreted as raw text must be on a seperate line to what appears as a str. 
After using the template language for a bit, this isn't as bad as it sounds, as it forces you to keep anything you're
assigning/printing seperate, but I will consider modifying this so that lines at the same level without a blank line 
between them are compressed into one line.

rendering templates
-------------------

There are several ways you can render templates. the easiest way being to use the Controller class, and 
view(self, model = None, template='') method, passing your template and view model as a parameter, this method will 
then ensure your template is compiled (if it needs compiling) and it's output is placed in a response.

Routing
=======

Currently, mvc uses a base Route() object stored in mvc.routing.route.route_map. This should change in the future to 
better restructure the system.

Routes themselves refer to a callable, or a child routes, and a regex string to match incoming urls.

When you add a url to the application's route_map, it's broken up into its component parts and stored as a tree.

There are then several ways you can apply your routes, detailed below.

note, routes always start with a /, and the ^ and $ in the regex routes are automatically applied when resolving the
route_map

decorators
----------

flask-esque routes can be created by adding named parameters as arguments

    @route('/my/url/(?P<id>[0-9]{2})')
    def my_action(self, id):
        pass

route_map appending
-------------------

you can also work with the routes directly using django-esque routing

    route_map += Route('/my/url/(?P<id>[0-9]{2})', my_action)

it's worth adding, that my_action could easily be another Route(), or you could store a route you create and call += on
it as well and the routemap would have the routes you've passed added too them at the point you have added them.

With either method, as long as your code is hit, either by import, function call, or keeping your entire site in one file
the routing will work with either method, interchangably.

example
-------

Check out https://github.com/SilentPenguin/mvc-example for a working example using route_map appending.
