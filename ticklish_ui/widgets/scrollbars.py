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

"""Defines the ticklish_ui Scrollbar and Scrollable widgets. """
import tkinter as tk
import tkinter.ttk as ttk
from ticklish_ui.widgets.factories import WidgetFactory, ContainerFactory

class Scrollbar(WidgetFactory):
    """ Wrapper for the tkinter.ttk.Scrollbar class. """
    def __init__(self, orient):
        """ Initialize the Scrollbar.

        Arguments:
            orient - a string, either 'vertical' or 'horizontal'
        """
        super().__init__(ttk.Scrollbar)
        self.kwargs['orient'] = orient

class Scrollable(ContainerFactory):
    """A frame with scrollable area and pre-attached scrollbars.

    Scrollable is a container, like a frame, which takes rows of
    widgets as input. By default, Scrollable will have a vertical
    scrollbar only. Which scrollbars are visible can be customized
    using the options() method with options 'vertical' and
    'horizontal' being set to True, if the scrollbar should be added
    and False if it should not.

    Example:
        from ticklish_ui import *

        app = Application(
            '',
            [Scrollable(
                [Label('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')],
            ).options(width=100, height=20, vertical=False, horizontal=True)]
        )

    All widgets contained in the Scrollable container will have the
    class 'Scrollable' which can be used to filter event streams or
    with the tkinter bind_class() method.

    Example (continued):
        (app.get_event_stream('<Button>')
         .by_class('Scrollable')
         .map(lambda e: print('Event stream'))
        )

        app.bind_class('Scrollable', '<Button>', lambda e: print('bind_class'))
        app.mainloop()

    The scroll area, a Canvas widget, and scrollbars can be accessed
    like so:

    Example:
        app = Application(
            'Scrollbars Access',
            # .row1
            [Scrollable().options(name='scrollable', horizontal=True, vertical=True)]
        )

        # The container as a whole.
        scrollable = app.nametowidget('.row1.scrollable')

        # The canvas.
        scrollarea = app.nametowidget('.row1.scrollable.scrollarea')

        # The scrollbars.
        vertical = app.nametowidget('.row1.scrollable.verticalscroll')
        horizontal = app.nametowidget('.row1.scrollable.horizontalscroll')

    """
    def __init__(self, *rows):
        """Initialize the Scrollable widget.

        Arguments:
            *rows - any number of rows, each row given as a list of
                    ticklish_ui widgets.

        """
        super().__init__(ttk.Frame, rows)
        self.canvas_args = {}
        self.frame_args = {}
        self.kwargs['tags'] = 'Scrollable'
        self.vertical = True
        self.horizontal = False

    def options(self, **kwargs):
        for key in kwargs:
            if key in ['width', 'height']:
                self.canvas_args[key] = kwargs[key]
            elif key == 'vertical':
                self.vertical = kwargs[key]
            elif key == 'horizontal':
                self.horizontal = kwargs[key]
            elif key == 'tags':
                new_tags = f"{self.kwargs['tags']} {kwargs['tags']}"
                self.kwargs[key] = new_tags
            else:
                self.frame_args[key] = kwargs[key]
        return self

    def create_widget(self, parent):
        scrollable = ttk.Frame(parent, **self.frame_args)
        canvas = tk.Canvas(
            scrollable, name='scrollarea', **self.canvas_args
        )
        tags = tuple(self.kwargs['tags'].strip().split(' '))
        canvas.bindtags(tags + canvas.bindtags())
        content = super().create_widget(canvas)
        if self.vertical:
            v_bar = ttk.Scrollbar(
                scrollable, name='verticalscroll',
                orient='vertical', command=canvas.yview
            )
            v_bar.grid(row=0, column=1, sticky='ns')
            canvas['yscrollcommand'] = v_bar.set


        if self.horizontal:
            h_bar = ttk.Scrollbar(
                scrollable, name='horizontalscroll',
                orient='horizontal', command=canvas.xview
            )
            h_bar.grid(row=1, column=0, sticky='ew')
            canvas['xscrollcommand'] = h_bar.set

        scrollable.pack(fill='both')
        canvas.grid(row=0, column=0)
        canvas.create_window(0, 0, anchor='nw', window=content)

        scrollable.update_idletasks()
        canvas['scrollregion'] = canvas.bbox('all')
        return scrollable
