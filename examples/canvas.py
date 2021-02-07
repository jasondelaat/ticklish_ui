from ticklish_ui import *

app = Application(
    'Canvas Example',

    # .row1
    [Canvas(640, 480)],
)

def start_drawing(e):
    e.widget.drawing = True
    e.widget.last_x = e.x
    e.widget.last_y = e.y
    
def stop_drawing(e):
    e.widget.drawing = False

def draw(e):
    try:
        if e.widget.drawing:
            x, y = e.widget.last_x, e.widget.last_y
            e.widget.last_x = e.x
            e.widget.last_y = e.y
            e.widget.create_line(x, y, e.x, e.y)
    except AttributeError:
        pass
    
press = app.get_event_stream('<Button-1>').by_class('Canvas')
release = app.get_event_stream('<ButtonRelease-1>').by_class('Canvas')
move = app.get_event_stream('<Motion>').by_class('Canvas')

press.map(start_drawing)
press.map(lambda e: print('Started drawing'))

release.map(stop_drawing)
release.map(lambda e: print('Stopped drawing'))

move.map(draw)

app.mainloop()
