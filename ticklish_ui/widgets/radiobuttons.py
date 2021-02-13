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

"""Defines the ticklish_ui Radiobutton and RadioGroup widgets. """
import tkinter as tk
import tkinter.ttk as ttk
from ticklish_ui.widgets.frames import Frame
from ticklish_ui.widgets.factories import WidgetFactory

class Radiobutton(WidgetFactory):
    """ Wrapper for the tkinter.ttk.Radiobutton class. """
    def __init__(self, button_text):
        """Initialize the Radiobutton.

        Arugments:
            button_text - a string. The text and value of the
                          radiobutton are set to this value and the
                          name of the radiobutton is set to
                          'radio_{button_text}'

        """
        super().__init__(ttk.Radiobutton)
        self.kwargs['text'] = button_text
        self.kwargs['value'] = button_text

class RadioGroup(Frame):
    """Create a set of radio buttons.

    RadioGroup is a ticklish addition which creates a set of radio
    buttons from a list of strings.

    """
    def __init__(self, group_name, *rows):
        """Initialize the RadioGroup.

        The frame containing the radio buttons will be given the name
        group_name, each button will be given the name
        radio_{option}, and all radio buttons in the group will be
        assigned group_name capitalized as their class_ option.

        For instance, given group_name = alpha, and
        options = ['A', 'B', 'C']:

        1. The frame will be called alpha
        2. The buttons will be called radio_A, radio_B, and radio_C
        3. All three buttons' class_ option will be Alpha

        Arguments:
            group_name - a string, the name of the group. Radio
                         buttons in this group will have this as as
                         their class_ attribute.

            options - a list of strings. Each string becomes a
                      separate radio button in the group.

        """
        button_rows = []
        for row in rows:
            buttons = map(lambda label: Radiobutton(label).options(
                class_=group_name.capitalize(),
                name=f'radio_{label}'
            ), row)
            button_rows.append(buttons)
        super().__init__(*button_rows)
        self.kwargs['name'] = group_name

    def create_widget(self, parent):
        widget = super().create_widget(parent)
        widget.variable = tk.StringVar()
        for row in widget.winfo_children():
            for button in row.winfo_children():
                button.configure(variable=widget.variable)
                tags = list(button.bindtags())
                tags.insert(1, 'TRadiobutton')
                button.bindtags(tags)
        return widget
