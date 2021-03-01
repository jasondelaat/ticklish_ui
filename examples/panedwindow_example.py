# Demonstrates the PanedWindow widget.

from ticklish_ui import *

def make_frame(n):
    return Frame(
        # .row1
        [Text(f'Some text in pane {n}')]
    )

app = Application(
    'PanedWindow Example',
    # .row1
    [PanedWindow(
        (1, make_frame(1)),
        (3, make_frame(2))
    ).options(orient='horizontal', width=640)
    ]
)

app.mainloop()
