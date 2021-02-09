# Demonstrates using a LabelFrame.
from ticklish_ui import *

Application(
    'Label Frame Example',
    [LabelFrame(
        'Buttons',
        [Button('Button 1'), Button('Button 2'), Button('Button 3')],
    )],
    [CloseButton('Quit')]
).mainloop()
