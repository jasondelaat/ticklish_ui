"""Defines the ticklish_ui Listbox widget. """
import tkinter as tk
import tkinter.ttk as ttk
from ticklish_ui.widgets.factories import WidgetFactory

class Listbox(WidgetFactory):
    """A wrapper for the tkinter.ttk.Treeview class.

    Listbox always displays its items as flat hierarchy. Each item's
    iid property is set to be the same as its text so a call to the
    widget's focus() method will return the item text.

    """
    def __init__(self, items):
        """ Initialize the Listbox.

        Arguments:
            items - a list of strings to be displayed in the Listbox.
        """
        super().__init__(ttk.Treeview)
        self.items = items

    def create_widget(self, parent):
        tree = super().create_widget(parent)
        for i in range(len(self.items)):
            tree.insert('', i, iid=self.items[i], text=self.items[i])
        tree.pack(side=tk.LEFT)
        return tree
