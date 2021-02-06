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
        ttk.Style().theme_use('aqua')


    def get_event_stream(self, event_sequence):
        stream = events.EventStream()
        self.bind_all(event_sequence, lambda e: stream.insert(e))
        return stream
        
class _Toplevel(tk.Toplevel):
    def __init__(self, title):
        super().__init__()
        self.title(title)
        ttk.Style().theme_use('aqua')

def Application(title, *rows):
    app = _Application(title)
    count = 0
    for row in rows:
        count += 1
        frame = ttk.Frame(app, name=f'row{count}')
        frame.pack(fill=tk.BOTH)
        for widget in row:
            w = widget(frame)
            w.pack(side=tk.LEFT)
    return app

def Toplevel(title, *rows):
    popup = _Toplevel(title)
    count = 0
    for row in rows:
        count += 1
        frame = ttk.Frame(popup, name=f'row{count}')
        frame.pack(fill=tk.BOTH)
        for widget in row:
            w = widget(frame)
            w.pack(side=tk.LEFT)
    return popup

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

class RadioGroup(_WidgetFactory):
    def __init__(self, group_name, options=[]):
        self.kwargs = {'name' : f'radiogroup_{group_name}'}
        self.group_name = group_name
        self.radio_options = options

    def __call__(self, parent):
        group = ttk.Frame(parent, **self.kwargs)
        group.pack(fill=tk.BOTH)
        control = tk.StringVar()
        for option in self.radio_options:
            button = ttk.Radiobutton(
                group, value=option, text=option, variable=control,
                class_=self.group_name, name=f'radio_{option}'
            )
            tags = list(button.bindtags())
            tags[0] = 'TRadiobutton'
            button.bindtags(tags)
            button.pack(side=tk.LEFT)
        control.set(self.radio_options[0])
        group.variable = control
        return group
