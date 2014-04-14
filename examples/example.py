from mvc.controller.controller import Controller

#the most basic a controller can get, it does nothing.

class Example(Controller):
    @get
    def my_action(self):
        self.not_found()

    @post
    def my_action(self, posted_form):
        self.not_found()
