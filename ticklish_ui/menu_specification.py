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
"""Provides the MenuSpecification class for defining hierarchical menus."""

class MenuSpecification:
    """Provides an interface for defining hierarchical menus.

    Example:
        menu = MenuSpecification()
        menu('One', 'Two', 'Three')
        menu.One('A', 'B', 'C')
        menu.One.A('Apple', 'Banana', 'Cherry')
        menu.Two('D', 'E', 'F')
        menu['Three']('G', 'H', 'I')

    Each sub-menu, once created, can be accessed either via the dot
    operator (menu.One) or by indexing (menu['Three']) and called as a
    function to define the entries of that sub-menu. Sub-menus can be
    nested arbitrarily deeply.

    The above example creates a menu with the following structure:

    One   - A - Apple
              - Banana
              - Cherry
          - B
          - C
    Two   - D
          - E
          - F
    Three - G
          - H
          - I

    """
    def __init__(self):
        self.items = []

    def __call__(self, *items):
        self.items = items
        for item in items:
            self.__dict__[item] = MenuSpecification()

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def finalize(self):
        """Creates the menu data structure.

        The finalize method turns the MenuSpecification into a list of
        2-tuples of the form (name, submenu) where 'name' is the name
        of the menu and 'submenu' is another list of 2-tuples. If
        'submenu' is an empty list then 'name' is just a normal menu
        item.

        It is not usually necessary to call finalize explicitly since
        any operation requiring a MenuSpecification will do so
        automatically.

        """
        spec = []
        for i in self.items:
            try:
                sub = self.__dict__[i].finalize()
                spec.append((i, sub))
            except AttributeError:
                spec.append(i)
        return spec
