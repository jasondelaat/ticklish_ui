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

"""Defines the ticklish_ui Application root widget. """
import tkinter as tk
import tkinter.ttk as ttk
import ticklish_ui.events as events
from ticklish_ui.widgets.factories import ContainerFactory

class Application(ContainerFactory, tk.Tk):
    """The root window for all ticklish UIs.

    This class wraps the tkinter.Tk class so every ticklish UI must
    contain exactly one instance of Application.

    """
    def __init__(self, title, *rows):
        """Initialize the Application.

        Arguments:
            title - a string, the name of the window displayed in the
                    titlebar.
            *rows - any number of rows given as lists of ticklish widgets.

        """
        super().__init__(None, rows)
        self.create_widget(None)
        self.title(title)
        self.style = ttk.Style()
        self.style.theme_use('default')
        self.event_streams = {}

    def event_generate(self, sequence, **args):
        """Overrides Tk.event_generate() to allow virtual event user data.

        The underlying tcl/tk implementation allows for user data to
        be attached to virtual events when generated. Tkinter,
        however, does not support this functionality.

        This override allows users to attach user data to virtual
        events when using event streams by intercepting the event,
        attaching the data and then inserting it into the stream. If
        not using event streams to handle events, this method simply
        falls back on Tk.event_generate() and custom user data will
        not work.

        Example:
            app = Application('User Data')
            app.get_event_stream('<<MyEvent>>').map(lambda e: print(e.data))
            app.event_generate('<<MyEvent>>', data=['this', 'is', 'my', 'data'])
            app.event_generate('<<MyEvent>>', data='any kind of data works')
            app.mainloop()

        The 'data' can be anything.
        """
        stream = self.event_streams.get(sequence, None)
        if (stream and sequence.startswith('<<') and 'data' in args):
            data = args['data']
            del args['data']

            def stream_handler(event):
                event.data = data
                stream.insert(event)

            self.bind_all(sequence, stream_handler)
        elif stream and sequence.startswith('<<'):
            self.bind_all(sequence, stream.insert)
        super().event_generate(sequence, **args)

    def get_event_stream(self, event_sequence):
        """Bind an event stream to the Application.

        See Stream and EventStream for how to use streams to implement
        UI functionality.

        Arguments:
            event_sequence - a string specifying the event to
                             bind. See the tkinter documentation for
                             how to specify event sequences.

        Returns:
            An EventStream object.

        """
        stream = self.event_streams.get(event_sequence, None)
        if not stream:
            stream = events.EventStream()
            self.event_streams[event_sequence] = stream
            self.bind_all(event_sequence, stream.insert)
        return stream

    def menubar(self, *menus):
        """Define the application menus.

        Arguments:
            *menus - any number of menu definitions. Each menu
                     definition is given as a 2-tuple. The first
                     element is the menu name, the second element is a
                     list of strings defining the items in the menu.

        """
        menubar = tk.Menu(self, name='menubar')
        self['menu'] = menubar
        for menu_label, items in menus:
            menu = tk.Menu(menubar)
            menubar.add_cascade(label=menu_label, menu=menu)
            for item in items:
                menu.add_command(
                    label=item, command=_menu_update(self, menu_label, item)
                )

    def menu_command(self, menu_selector, callback):
        """Bind a command to a menu item.

        Arguments:
            menu_selector - a string of the form {Menu}-{Item}. For
                            instance, given a menu Background with
                            entries Red, Green and Blue, the
                            menu_selector to bind a command to Red
                            would be 'Background-Red'
            callback - a function to call when the given menu item is
                       selected. The callback takes the root window as
                       input so the application can be manipulated in
                       any way the user requires.

        """
        (self.get_event_stream(f'<<Menu-{menu_selector}>>')
         .map(lambda e: callback(self))
        )

def _menu_update(root, label, item):
    def command():
        root.event_generate(f'<<Menu-{label}-{item}>>')
    return command
