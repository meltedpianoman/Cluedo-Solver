from cluedo.notebook import *


class Cluedo:

    def __init__(self):
        self.notebook = Notebook()

    def get_notebook(self):
        return self.notebook

    def make_note(self, subject, innocent):
        self.notebook.make_note(subject, innocent)
        
    # make_suggestion(self)
