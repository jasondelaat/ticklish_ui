class Stream:
    def __init__(self, predicate=lambda e: True, action=lambda e: e):
        self.predicate = predicate
        self.action = action
        self.children = []

    def filter(self, predicate):
        stream = self.__class__(predicate, lambda e: e)
        self.children.append(stream)
        return stream

    def map(self, action):
        stream = self.__class__(lambda e: True, action)
        self.children.append(stream)
        return stream
        
class EventStream(Stream):
    pass
