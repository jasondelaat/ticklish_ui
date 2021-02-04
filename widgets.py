import tkinter as tk
import tkinter.ttk as ttk

WIDGETS = {}

def Application(*rows):
    return tk.Tk()

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
