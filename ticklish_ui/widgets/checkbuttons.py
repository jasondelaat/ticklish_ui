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

"""Defines the ticklish_ui Checkbutton and CheckGroup widgets. """
import tkinter as tk
import tkinter.ttk as ttk
from ticklish_ui.widgets.frames import Frame
from ticklish_ui.widgets.factories import WidgetFactory

class Checkbutton(WidgetFactory):
    """Wrapper for the tkinter.ttk.Checkbutton class.

    Each checkbutton, when instantiated by create_widget(), has the
    get() and set() methods of its control variable (an IntVar) bound
    directly to the widget itself.

    Example:
        def checkbutton_handler(event):
            checkbutton = event.widget
            state = checkbutton.get() # 1 - checked, 0 - unchecked
            checkbutton.set(0)        # set the checkbutton to unchecked

    """
    def __init__(self, button_text):
        """Initialize the Checkbutton.

        Arguments:
            button_text - a string, the text that will be displayed
                          beside the checkbutton.

        """
        super().__init__(ttk.Checkbutton)
        self.kwargs['text'] = button_text

    def create_widget(self, parent):
        checkbutton = super().create_widget(parent)
        variable = tk.IntVar()
        checkbutton['variable'] = variable
        checkbutton.set = variable.set
        checkbutton.get = variable.get
        tags = list(checkbutton.bindtags())
        tags.insert(1, 'TCheckbutton')
        checkbutton.bindtags(tags)
        return checkbutton

class CheckGroup(Frame):
    """Create a set of check buttons.

    CheckGroup is a ticklish addition which creates a set of check
    buttons from a list of strings.

    """
    def __init__(self, group_name, *rows):
        """Initialize the CheckGroup.

        The frame containing the check buttons will be given the name
        group_name, each button will be given the name check_{option},
        and all radio buttons in the group will be assigned group_name
        capitalized as their class_ option.

        For instance, given group_name = alpha, and
        options = ['A', 'B', 'C']:

        1. The frame will be called alpha
        2. The buttons will be called check_A, check_B, and check_C
        3. All three buttons' class_ option will be Alpha

        Arguments:
            group_name - a string, the name of the group. Check
                         buttons in this group will have this as as
                         their class_ attribute.

            options - a list of strings. Each string becomes a
                      separate check button in the group.

        """
        check_rows = []
        for row in rows:
            check_row = map(
                lambda label: Checkbutton(label).options(
                    class_=group_name.capitalize(), name=f'check_{label}'
                ),
                row
            )
            check_rows.append(check_row)
        super().__init__(*check_rows)
        self.kwargs['name'] = group_name
