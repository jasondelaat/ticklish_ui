class Presenter:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.selections = []

        (view.get_event_stream('<<AddVertex>>')
         .map(self._get_coordinates)
         .map(self._add_vertex)
         .map(self._draw_vertex('black'))
        )
        
        (view.get_event_stream('<<SelectVertex>>')
         .map(self._get_coordinates)
         .map(self._find_vertex)
         .filter(self._vertex_exists)
         .map(self._cache_vertex)
         .map(self._draw_vertex('red'))
        )
        
        (view.get_event_stream('<<AddEdge>>')
         .filter(self._two_selections)
         .map(self._add_edge)
         .map(self._update_display)
         .map(self._clear_selections)
        )
        
    def _update_display(self, _argument_ignored):
        self.view.clear()
        for v in self.model.vertices:
            self.view.draw_vertex('black', v)

        for e in self.model.edges:
            self.view.draw_edge(e)

    def _cache_vertex(self, vertex):
        self.selections.append(vertex)
        return vertex
    
    def _vertex_exists(self, vertex):
        return vertex is not None

    def _clear_selections(self, _argument_ignored):
        self.selections = []
        
    def _add_edge(self, _event_ignored):
        return self.model.add_edge(*self.selections)

    def _two_selections(self, _event_ignored):
        return len(self.selections) == 2

    def _get_coordinates(self, event):
        return event.x, event.y
    
    def _add_vertex(self, coordinates):
        return self.model.add_vertex(*coordinates)

    def _draw_vertex(self, color):
        def handler(vertex):
            self.view.draw_vertex(color, vertex)
        return handler

    def _find_vertex(self, coordinates):
        return self.model.find_vertex(*coordinates)
        
    def start(self):
        self.view.mainloop()
