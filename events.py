class EventStream:
    def __init__(self, predicate=lambda e: True, action=lambda e: e):
        self.predicate = predicate
        self.action = action
