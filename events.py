class EventStream:
    def __init__(self, predicate=lambda e: True, action=lambda e: e):
        self.predicate = predicate
        self.action = action
        self.children = []

    def filter(self, predicate):
        stream = EventStream(predicate, lambda e: e)
        self.children.append(stream)
        return stream
