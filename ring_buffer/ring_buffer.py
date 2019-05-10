class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        # append an element at the end of the buffer
        self.storage.append(item)
        if len(self.storage) == self.capacity:
            self.current
        pass

    def get(self):
        # new array created to add all elements in array that have a value
        ringArray = []

    # for loop to ensure only values and not value None are added to array
        for i in self.storage:
            if i is not None:
                ringArray.append(i)
                return ringArray
