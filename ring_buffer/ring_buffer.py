class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [0] * capacity
        self.oldest = 0

    def append(self, item):
        # check if space available
        if None in self.storage:
            for i in self.storage:
                if self.storage[i] == 0:
                    self.storage[i] = item
                    break
                else:
                    continue
        
        # otherwise buffer is full
        elif None not in self.storage:
            self.storage[self.oldest] = item
            
            # increment oldest value
            self.oldest += 1
            if self.oldest >= len(self.storage):
                self.oldest = 0
        

    def get(self):
        return [i for i in self.storage if i != 0]