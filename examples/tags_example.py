# This example shows how to use the tags option.
from ticklish_ui import *

app = Application(
    'Tags Example',
    [Button('1').options(tags='tk_bind stream'),
     Button('2').options(tags='tk_bind'),
     Button('3').options(tags='stream'),
    ],
    [Frame(
        [Label(' L1 '),
         Label(' L2 '),
         Label(' L3 '),
        ]
    ).options(tags='tag_all')
    ]
)

app.bind_class('tk_bind', '<Button>', lambda e: print('tk_bind'))

(app.get_event_stream('<Button>')
 .by_class('stream')
 .map(lambda e: print('stream'))
)

(app.get_event_stream('<Button>')
 .by_class('tag_all')
 .map(lambda e: print('Got `em all!'))
)

app.mainloop()
