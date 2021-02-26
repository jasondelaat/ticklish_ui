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
        self.kwargs = {'tags' : ''}

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
            if key == 'tags':
                new_tags = ' '.join([self.kwargs['tags'], kwargs['tags']])
                self.kwargs['tags'] = new_tags
            else:
                self.kwargs[key] = kwargs[key]
        return self

    def create_widget(self, parent):
        """Creates the actual underlying widget.

        Arguments:
            parent - a widget which will contain the widget being created.

        Returns:
            A new widget.

        """
        tags = self.kwargs['tags'].strip().split(' ')
        del self.kwargs['tags']
        widget = self.widget_type(parent, **self.kwargs)
        widget.tags = tags
        widget.bindtags(tuple(tags) + widget.bindtags())
        return widget

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
        tags_string = self.kwargs['tags']
        tags = tuple(tags_string.strip().split(' '))
        del self.kwargs['tags']
        if self.widget_type:
            container = self.widget_type(parent, **self.kwargs)
            container.bindtags(tags + container.bindtags())
        else:
            container = self
        count = 0
        for row in self.child_rows:
            count += 1
            frame = ttk.Frame(container, name=f'row{count}')
            frame.bindtags(tags + frame.bindtags())
            frame.pack(fill=tk.BOTH)
            for factory in row:
                widget = factory.options(tags=tags_string).create_widget(frame)
                widget.pack(side=tk.LEFT)
        return container
