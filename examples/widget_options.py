# The example demonstrates the use of the options method on widgets.

from ticklish_ui import *

Application(
    'Options Example',

    # .row1
    [Label('Red text!').options(foreground='red')]
).mainloop()
