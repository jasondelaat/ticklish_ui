# This example demonstates how to use and capture events on the
# Scrollable container widget.
from ticklish_ui import *

app = Application(
    '',
    # .row1
    [Scrollable(
        [Label('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')],
        [Label('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')],
        [Label('cccccccccccccccccccccccccccccccccccccccccccc')],
        [Label('dddddddddddddddddddddddddddddddddddddddddddd')],
        [Label('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')],
        [Label('ffffffffffffffffffffffffffffffffffffffffffff')],
        [Label('gggggggggggggggggggggggggggggggggggggggggggg')],
        [Label('hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')],
        [Label('iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')],
        [Label('jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj')],
        [Label('kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')],
        [Label('llllllllllllllllllllllllllllllllllllllllllll')],
        [Label('mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm')],
        [Label('nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn')],
        [Label('oooooooooooooooooooooooooooooooooooooooooooo')],
        [Label('pppppppppppppppppppppppppppppppppppppppppppp')],
        [Label('qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq')],
        [Label('rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr')],
        [Label('ssssssssssssssssssssssssssssssssssssssssssss')],
        [Label('tttttttttttttttttttttttttttttttttttttttttttt')],
        [Label('uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu')],
        [Label('vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv')],
        [Label('wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww')],
        [Label('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')],
        [Label('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')],
        [Label('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')],
    ).options(name='scroll', width=300, height=100, horizontal=True)]
)

def scroll_region(event):
    canvas = app.nametowidget('.row1.scroll.scrollarea')
    canvas.yview_scroll(event.delta, 'units')

(app.get_event_stream('<MouseWheel>')
 .by_class('Scrollable')
 .map(scroll_region)
)

app.mainloop()
