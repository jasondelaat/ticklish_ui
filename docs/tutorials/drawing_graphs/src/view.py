from ticklish_ui import *

class GraphView:
    def __init__(self):
        self.ui = Application(
            'Graphs',
            [RadioGroup('mode', ['Vertex', 'Edge'])],
            [Canvas(640, 480).options(name='canvas')],
        )

        self._set_mode('Vertex')
        self.canvas = self.ui.nametowidget('.row2.canvas')

        click = self.ui.get_event_stream('<ButtonRelease-1>').by_name('canvas')

        (click
         .filter(self._mode_equals('Vertex'))
         .map(self._event_generate('<<AddVertex>>'))
        )

        (click
         .filter(self._mode_equals('Edge'))
         .map(self._event_generate('<<SelectVertex>>'))
         .map(self._event_generate('<<AddEdge>>'))
        )

    def _mode_equals(self, mode):
        def handler(_event_ignored):
            set_mode = self.ui.nametowidget('.row1.mode').variable.get()
            return set_mode == mode
        return handler

    def _set_mode(self, mode):
        self.ui.nametowidget('.row1.mode').variable.set(mode)

    def _event_generate(self, event_sequence):
        def handler(event):
            self.ui.event_generate(event_sequence, x=event.x, y=event.y)
            return event
        return handler

    def draw_vertex(self, color, vertex):
        x1, y1 = vertex.x - 3, vertex.y - 3
        x2, y2 = vertex.x + 3, vertex.y + 3
        self.canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color)

    def draw_edge(self, edge):
        x1, y1 = edge.start.x, edge.start.y
        x2, y2 = edge.end.x, edge.end.y
        self.canvas.create_line(x1, y1, x2, y2)

    def clear(self):
        self.canvas.delete('all')

    def get_event_stream(self, event_sequence):
        return self.ui.get_event_stream(event_sequence)

    def mainloop(self):
        self.ui.mainloop()
    
        
