import tkinter as tk
import tkinter.ttk as ttk

WIDGETS = {
    'Button' : ttk.Button,
}

class _Application(tk.Tk):
    def __init__(self):
        super().__init__()
        
def Application(*rows):
    app = _Application()
    for row in rows:
        for widget in row:
            w = widget(app)
            w.pack()
    return app

def Button(button_text):
    return _WidgetFactory('Button').options(text=button_text)

class _WidgetFactory:
    def __init__(self, widget_type):
        self.widget_type = widget_type
        self.kwargs = {}

    def options(self, **kwargs):
        for key in kwargs:
            self.kwargs[key] = kwargs[key]
        return self

    def __call__(self, parent):
        return WIDGETS[self.widget_type](parent, **self.kwargs)
