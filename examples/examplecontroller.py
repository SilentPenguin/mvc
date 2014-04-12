from mvc import Controller

#the most basic a controller can get, it does nothing.

class MyController (Controller):
    @get
    def my_action(self):
        pass

    @post
    def my_action(self, posted_form):
        pass
