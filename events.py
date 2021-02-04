class Stream:
    def __init__(self, predicate=lambda e: True, action=lambda e: e):
        self.predicate = predicate
        self.action = action
        self.children = []

    def filter(self, predicate):
        stream = self.__class__(predicate, lambda e: e)
        self.children.append(stream)
        return stream

    def insert(self, value):
        if self.predicate(value):
            new_value = self.action(value)
            for child in self.children:
                child.insert(new_value)
                
    def map(self, action):
        stream = self.__class__(lambda e: True, action)
        self.children.append(stream)
        return stream
        
class EventStream(Stream):
    def by_name(self, widget_name):
        return self.filter(lambda e: e.widget.winfo_name() == widget_name)

    def by_class(self, widget_class):
        return self.filter(lambda e: e.widget.winfo_class() == widget_class)
