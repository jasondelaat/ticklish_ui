# BSD 3-Clause License
#
# Copyright (c) 2021, Jason DeLaat
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

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
