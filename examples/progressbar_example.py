from ticklish_ui import *

app = Application(
    'Progressbar',
    [Progressbar().options(name='pb1')],
    [Progressbar('indeterminate').options(name='pb2')]
)

app.nametowidget('.row1.pb1').start(1)
app.nametowidget('.row2.pb2').start(1)

app.mainloop()
