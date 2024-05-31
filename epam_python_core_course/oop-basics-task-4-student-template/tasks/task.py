class HistoryDict:
    def __init__(self, initial_data=None):
        self.data = initial_data if initial_data is not None else {}
        self.history = []

    def set_value(self, key, value):
        self.data[key] = value
        self.history.append(key)
        if len(self.history) > 5:
            self.history.pop(0)
    
    def get_history(self):
        return self.history
    
