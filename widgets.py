import tkinter as tk
import tkinter.ttk as ttk
import events

WIDGETS = {
    'Button' : ttk.Button,
    'Entry' : ttk.Entry,
    'Label' : ttk.Label,
}

class _Application(tk.Tk):
    def __init__(self, title):
        super().__init__()
        self.title(title)

    def get_event_stream(self, event_sequence):
        stream = events.EventStream()
        self.bind_all(event_sequence, lambda e: stream.insert(e))
        return stream
        
def Application(title, *rows):
    app = _Application(title)
    count = 0
    for row in rows:
        count += 1
        frame = tk.Frame(app, name=f'row{count}')
        frame.pack()
        for widget in row:
            w = widget(frame)
            w.pack(side=tk.LEFT)
    return app

def Button(button_text):
    return _WidgetFactory('Button').options(text=button_text)

def Entry():
    return _WidgetFactory('Entry')

def Label(label_text):
    return _WidgetFactory('Label').options(text=label_text)

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
