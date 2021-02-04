import tkinter as tk
import tkinter.ttk as ttk

WIDGETS = {}

def Application(*rows):
    return tk.Tk()

class _WidgetFactory:
    def __init__(self, widget_type):
        self.widget_type = widget_type

    def options(self, **kwargs):
        self.kwargs = kwargs
        return self

    def __call__(self, parent):
        return WIDGETS[self.widget_type](parent, **self.kwargs)
        
