# Another example of Scrollable with two scrollable areas.
from ticklish_ui import *

app = Application(
    'Second Scrollbar Example',
    [Scrollable(
        [Label(1)],
        [Label(2)],
        [Label(3)],
        [Label(4)],
        [Label(5)],
        [Label(6)],
        [Label(7)],
        [Label(8)],
        [Label(9)],
        [Label(10)],
    ).options(name='scroll1', tags='scroll1', width=100, height=50)],
    [Scrollable(
        [Label('A')],
        [Label('B')],
        [Label('C')],
        [Label('D')],
        [Label('E')],
        [Label('F')],
        [Label('G')],
        [Label('H')],
        [Label('I')],
        [Label('J')],
    ).options(name='scroll2', tags='scroll2', width=100, height=50)],
)

def scroll_region(widget_name):
    def handler(event):
        scrollarea = app.nametowidget(f'{widget_name}.scrollarea')
        scrollarea.yview_scroll(event.delta, 'units')
    return handler

wheel = app.get_event_stream('<MouseWheel>').by_class('Scrollable')

(wheel
 .by_class('scroll1')
 .map(scroll_region('.row1.scroll1'))
)

(wheel
 .by_class('scroll2')
 .map(scroll_region('.row2.scroll2'))
)

app.mainloop()
