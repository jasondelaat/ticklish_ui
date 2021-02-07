import tkinter as tk
import tkinter.ttk as ttk
import ticklish_ui.events as events

class _WidgetFactory:
    def __init__(self, widget_type):
        self.widget_type = widget_type
        self.kwargs = {}

    def options(self, **kwargs):
        for key in kwargs:
            self.kwargs[key] = kwargs[key]
        return self

    def __call__(self, parent):
        self.widget = self.widget_type(parent, **self.kwargs)
        return self.widget

class Application(tk.Tk):
    def __init__(self, title, *rows):
        super().__init__()
        self.title(title)
        self.style = ttk.Style()
        self.style.theme_use('aqua')
        count = 0
        for row in rows:
            count += 1
            frame = ttk.Frame(self, name=f'row{count}')
            frame.pack(fill=tk.BOTH)
            for widget in row:
                w = widget(frame)
                w.pack(side=tk.LEFT)

    def get_event_stream(self, event_sequence):
        stream = events.EventStream()
        self.bind_all(event_sequence, lambda e: stream.insert(e))
        return stream
        
def Button(button_text):
    return _WidgetFactory(ttk.Button).options(text=button_text)

class Canvas(_WidgetFactory):
    def __init__(self, width, height):
        self.kwargs = {'width' : width, 'height' : height}

    def __call__(self, parent):
        return tk.Canvas(parent, **self.kwargs)

def CloseButton(button_text):
    button_factory = _WidgetFactory(ttk.Button) 
    return button_factory.options(
        text=button_text,
        command=lambda: button_factory.widget.winfo_toplevel().destroy()
    )

Entry = _WidgetFactory(ttk.Entry)

def Label(label_text):
    return _WidgetFactory(ttk.Label).options(text=label_text)

class Listbox(_WidgetFactory):
    def __init__(self, items):
        self.kwargs = {}
        self.items = items

    def __call__(self, parent):
        tree = ttk.Treeview(parent, **self.kwargs)
        for i in range(len(self.items)):
            tree.insert('', i, iid=self.items[i], text=self.items[i])
        tree.pack(side=tk.LEFT)
        return tree

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
            tags.insert(1, 'TRadiobutton')
            button.bindtags(tags)
            button.pack(side=tk.LEFT)
        control.set(self.radio_options[0])
        group.variable = control
        return group

class Toplevel(tk.Toplevel):
    def __init__(self, title, *rows):
        super().__init__()
        self.title(title)
        self.style = ttk.Style()
        self.style.theme_use('aqua')
        count = 0
        for row in rows:
            count += 1
            frame = ttk.Frame(self, name=f'row{count}')
            frame.pack(fill=tk.BOTH)
            for widget in row:
                w = widget(frame)
                w.pack(side=tk.LEFT)
