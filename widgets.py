import tkinter as tk
import tkinter.ttk as ttk

def Application(*rows):
    return tk.Tk()

class _WidgetFactory:
    def __init__(self, widget_type):
        self.widget_type = widget_type
        
