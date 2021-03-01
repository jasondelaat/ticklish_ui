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

"""Defines the widgets available is ticklish_ui.

In most cases widgets are wrapped tkinter or tkinter.ttk widgets. Some
widgets, like RadioGroup, are additions intended to make certain tasks
easier: rather than creating individual radio buttons, make a whole
set with a single command.

Widget initialization tries to take sensible minimum arguments to
display that widget. For instance, Labels and Buttons take a text
argument since both, typically, display text; Canvas takes a width and
height; and so on.

All ticklish UIs must start by defining an Application, which is the
root window of the UI, and calling it's mainloop. The minimal ticklish
UI is:

Example - Minimal UI - /examples/minimal_ui.py:
    # The smallest possible ticklish application.
    from ticklish_ui import *

    Application('Window Title').mainloop()

Widgets are added to an Application in rows, each row being given as a
list.  All widgets in a row are automatically packed into a frame and
the frames are named 'rowN' where 'N' is the row number starting at 1.

Example - UI Rows - /examples/ui_rows.py:
    # This example shows how widgets are packed into an application in rows.
    from ticklish_ui import *

    Application(
        'Application Rows',

        # .row1
        [Label('This is the first row.')],

        # .row2
        [Label('This is the second row.'), Label('Still the second row.')],

        # .row3
        [Label('Third row'), CloseButton('Quit')],
    ).mainloop()

In the above example, CloseButton is a ticklish addition which, when
clicked, automatically closes the toplevel window which contains it.

Additional options can be provided by calling the .options() method.

Example - Widget Options - /examples/widget_options.py:
    # The example demonstrates the use of the options method on widgets.

    from ticklish_ui import *

    Application(
        'Options Example',

        # .row1
        [Label('Red text!').options(foreground='red')]
    ).mainloop()

"""
from ticklish_ui.widgets.application import *
from ticklish_ui.widgets.buttons import *
from ticklish_ui.widgets.canvas import *
from ticklish_ui.widgets.checkbuttons import *
from ticklish_ui.widgets.combobox import *
from ticklish_ui.widgets.dropdown import *
from ticklish_ui.widgets.entry import *
from ticklish_ui.widgets.factories import *
from ticklish_ui.widgets.frames import *
from ticklish_ui.widgets.label import *
from ticklish_ui.widgets.listbox import *
from ticklish_ui.widgets.notebook import *
from ticklish_ui.widgets.panedwindow import *
from ticklish_ui.widgets.progressbar import *
from ticklish_ui.widgets.radiobuttons import *
from ticklish_ui.widgets.scale import *
from ticklish_ui.widgets.scrollbars import *
from ticklish_ui.widgets.text import *
from ticklish_ui.widgets.toplevel import *
