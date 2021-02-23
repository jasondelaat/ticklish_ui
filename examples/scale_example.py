from ticklish_ui import *

app = Application(
    'Scale Example',
    # Scale takes parameters from_, to, and value
    [Scale(0, 100, 75).options(name='scale1')],

    # Defaults are 0.0, 1.0, and 0.0
    [Scale().options(name='scale2')],

    # Can also be given as keywords
    [Scale(value=0, to=10, from_=-10).options(name='scale3')],
)

# When a scale changes it generates virtual event <<ScaleUpdate>>
(app.get_event_stream('<<ScaleUpdate>>')
 .map(lambda e: print(f'{e.widget.winfo_name()}: {e.widget.get()}'))
)

app.mainloop()

