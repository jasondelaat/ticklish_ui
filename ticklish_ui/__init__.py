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

"""A thin(-ish) wrapper around tkinter.

The ticklish_ui package is allows users to define GUI applications
declaratively and decouples event binding from GUI creation.

While ticklish is mostly just a wrapper around tkinter widgets some
'quality of life' additions have been made. Two examples:

    RadioGroup - automatically creates radio buttons from a list of
                 names so you don't have to create them all manually

    CloseButton - a button which automatically closes the toplevel
                  window that contains it.

ticklish uses themed tkinter widgets (ttk) when possible and falls
back to the base tkinter widget set otherwise.

Example:
    from ticklish_ui import *

    app = Application(
        'Example GUI',

        # .row1
        [Label('Enter some text below:')],

        # .row2
        [Entry().options(name='user_text')],

        # .row3
        [Button('OK').options(name='ok'), CloseButton('Quit')],
    )

    def show_text(event):
        text = app.nametowidget('.row2.user_text').get()
        return Toplevel(
            'Your Text',

            # .row1
            [Label(text)],

            # .row2
            [CloseButton('OK')],
        )

    (app.get_event_stream('<ButtonRelease-1>')
    .by_name('ok')
    .map(show_text)
    )

    app.mainloop()

"""
from ticklish_ui.widgets import *
from ticklish_ui.events import *
