# This example demonstrates simple usage of the Text widget.

from ticklish_ui import *

app = Application(
    'Text Example',
    [Text('Hello world!').options(name='text_area')],
)

# Whatever is typed into the Text widget is echoed to the console.
(app.get_event_stream('<KeyPress>')
 .by_name('text_area')
 .map(lambda e: print(e.char, end='', flush=True))
)

app.mainloop()
