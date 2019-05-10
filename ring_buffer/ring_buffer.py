class RingBuffer:
  # based on FIFO
  # has two ends front and rear
  # insert from rear
  # delete from front
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        # append an element at the end of the buffer
        if self.current < len(self.storage):
            self.storage[self.current] = item
            self.current += 1
            return self.storage
        else:
            self.current = 0
        return self.append(item)

    def get(self):
            # new array created to add all elements in array that have a value
        ringArray = []

    # for loop to ensure only values and not value None are added to array
        for i in self.storage:
            if i is not None:
                ringArray.append(i)
                return ringArray
