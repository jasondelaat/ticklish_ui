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

"""Provides Streams for intercepting and manipulating events.

Event streams are how ticklish decouples GUI layout and event
handling. After defining an appliation, users retrieve event streams
and manipulate them to bind operations to specific GUI actions.

Stream and EventStream can be used mostly interchangably but
EventStream has additional methods specifically for matching GUI
events according to the widget name, widget class, etc.

Example 1 - No events - /examples/basic_stream.py:

    # This example creates a stream which filters out odd numbers and
    # prints only the even ones.

    from ticklish_ui import Stream

    stream = Stream()

    (stream
    .filter(lambda n: n % 2 ==0)
    .map(print)
    )

    stream.insert(1)
    stream.insert(2)
    stream.insert(3)
    stream.insert(4)
    stream.insert(5)
    stream.insert(6)
    stream.insert(7)
    stream.insert(8)
    stream.insert(9)
    stream.insert(10)

    # Expected output:
    # 2
    # 4
    # 6
    # 8
    # 10

Example 2 - Simple events - /examples/simple_events.py:

    # This example demonstrates simple use of event streams by creating
    # GUI with two buttons and binding multiple events to them.

    from ticklish_ui import *

    # Create the GUI
    app = Application(
        'EventStream Example',
        [Label("I'm a label. Clicking me won't do anything.")],
        [Button('Click me!'), Button('No, me!').options(name='button2')]
    )

    # Get an event stream of all clicks anywhere in the application
    # window.
    clicks = app.get_event_stream('<ButtonRelease-1>')

    # We can create new streams by filtering and mapping old ones:

    # This stream only captures clicks on Button widgets.
    any_button = clicks.filter(lambda e: e.widget.winfo_class() == 'TButton')

    # And this one captures clicks on the second button only.
    button2_only = clicks.filter(lambda e: e.widget.winfo_name() == 'button2')

    # Multiple actions can be mapped to a single stream. These actions are
    # both performed when either button is clicked.
    any_button.map(lambda e: print('Clicked either button'))
    any_button.map(lambda e: print('but I don\'t know which one.'))

    # But this only happens when the second button is clicked.
    button2_only.map(lambda e: print('Clicked "No me!"'))

    app.mainloop()

"""

class Stream:
    """Create streamable data.

    Streams intercept, act on, and pass along data. New streams are
    created by filtering and mapping existing streams. A value
    inserted into a parent stream will be passed along to child
    streams, acted upon and potentially transformed before being
    passed along to grandchild streams, and so on. This process
    continues until the data is either filtered out or there are no
    more child streams.

    """
    def __init__(self, predicate=lambda e: True, action=lambda e: e):
        self.predicate = predicate
        self.action = action
        self.children = []

    def filter(self, predicate):
        """Creates a new stream applying a filter to its parent's data.

        Arguments:
            predicate - a function accepting a single value and
                        returns True if the data should be kept acted
                        upon by the new stream and False otherwise.

        Returns:
            A new Stream.

        """
        stream = self.__class__(predicate, lambda e: e)
        self.children.append(stream)
        return stream

    def insert(self, value):
        """Insert data into the stream.

        If the data is accepted by the stream's filter then it is
        acted upon and passed along to this stream's
        children. Otherwise, the data is discarded.

        Arguments:
            value - the data to pass into the stream

        """
        try:
            if self.predicate(value):
                new_value = self.action(value)
                for child in self.children:
                    child.insert(new_value)
        # This error can occur when a user clicks a CloseButton and
        # the window is destoyed but streams are still attempting to
        # process click events. This should be considered a temporary
        # fix.
        except AttributeError as error:
            # If this isn't the message then we're getting an error we
            # should probably care about.
            message = error.args[0]
            if message not in (
                    "'str' object has no attribute 'winfo_name'",
                    "'str' object has no attribute 'winfo_class'"
            ):
                raise error

    def map(self, action):
        """Creates a new stream applying an action to the stream's data.

        If the data is accepted by the stream's filter then perform
        the given action on it and pass the new data along to this
        stream's children.

        Arguments:
            action - a function accepting a single argument (the data
                     to act on). If this function returns a value,
                     that value will be passed along to child streams.

        Returns:
            A new Stream.

        """
        stream = self.__class__(lambda e: True, action)
        self.children.append(stream)
        return stream

class EventStream(Stream):
    """Streams for handling GUI events.

    EventStreams are Streams with a few extra methods specifically for
    working wth events generated by tkinter applications.

    See the Stream documentation for a fuller explanation of Streams.

    """

    def by_name(self, widget_name):
        """Match events on a specific widget.

        Arguments:
            widget_name - a string, the name of the widget either
                          assigned automatically by tkinter or by the
                          'name' option when creating the widget.

        Returns:
            A new Stream.

        """
        return self.filter(lambda e: e.widget.winfo_name() == widget_name)

    def by_class(self, widget_class):
        """Match events on all widgets of a specific class.

        Arguments:
            widget_class - a string, the name of the widget class
                           either assigned automatically or by the
                           'tags' option when creating the widget.

        Returns:
            A new Stream.

        """
        def handler(event):
            try:
                return widget_class in event.widget.bindtags()
            except AttributeError:
                return False
        return self.filter(handler)
