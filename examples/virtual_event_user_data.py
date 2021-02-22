from ticklish_ui import *

def generate_virtual(user_data):
    def command():
        app.event_generate(
            '<<MyVirtualEvent>>',
            # user_data can be any type
            data=user_data,

            # And, of course, we can still attach normal attributes as
            # usual.
            x=100, y=200
        )
    return command

app = Application(
    'Virtual Event User Data',
    [Button(1).options(command=generate_virtual(1)),
     Button(2).options(command=generate_virtual('Two')),
     Button(3).options(command=generate_virtual([None, False, 3])),
     Button(4).options(command=generate_virtual({4 : 'Four'})),
    ]
)

# Shows that the user data has been set.
(app.get_event_stream('<<MyVirtualEvent>>')
 .map(lambda e: print(e.data))
)

# And that the normal event attributes are there too.
(app.get_event_stream('<<MyVirtualEvent>>')
 .map(lambda e: print(e.x, e.y))
)

app.mainloop()
