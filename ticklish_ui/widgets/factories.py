"""Defines the ticklish_ui WidgetFactory and ContainerFactory base classes. """
import tkinter as tk
import tkinter.ttk as ttk

class WidgetFactory:
    """Base class for most non-toplevel widgets.

    When defining an Application users are actually creating
    factories, which store the necessary information to create
    widgets, and not not widgets themselves. The actual widget is
    created later by Application, Toplevel, or other container
    widgets.

    """
    def __init__(self, widget_type):
        super().__init__()
        self.widget_type = widget_type
        self.kwargs = {}

    def options(self, **kwargs):
        """Set additional keyword options on widgets.

        The options are passed along to the underlying widget without
        error checks or modification. If the given options are not
        valid for the underlying widget and error will result when the
        widget is created.

        Arguments:
            kwargs - a keyword argument dictionary

        Returns:
            self

        """
        for key in kwargs:
            self.kwargs[key] = kwargs[key]
        return self

    def create_widget(self, parent):
        """Creates the actual underlying widget.

        Arguments:
            parent - a widget which will contain the widget being created.

        Returns:
            A new widget.

        """
        return self.widget_type(parent, **self.kwargs)

class ContainerFactory(WidgetFactory):
    """Base class for widgets which contain other widgets.

    ContainerFactory differs from WidgetFactory in that it is
    responsible for creating itself and all of it's children.

    """
    def __init__(self, container_type, rows):
        """Initialize the ContainerFactory.

        Arguments:
            container_type - a widget class such as tkinter.ttk.Frame
            rows - a list of lists of WidgetFactory instances

        """
        super().__init__(container_type)
        self.child_rows = rows

    def create_widget(self, parent):
        if self.widget_type:
            container = self.widget_type(parent, **self.kwargs)
        else:
            container = self

        count = 0
        for row in self.child_rows:
            count += 1
            frame = ttk.Frame(container, name=f'row{count}')
            frame.pack(fill=tk.BOTH)
            for factory in row:
                widget = factory.create_widget(frame)
                widget.pack(side=tk.LEFT)
        return container
