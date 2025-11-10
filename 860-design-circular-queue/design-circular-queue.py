class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.k = k
        self.queue = [] 

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if(len(self.queue)<self.k):
            self.queue.append(value)
            return True
        return False

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.queue: 
            self.queue.pop(0)
            return True
        return False

    def Front(self):
        """
        :rtype: int
        """
        if self.queue:
            return self.queue[0]
        return -1

    def Rear(self):
        """
        :rtype: int
        """
        if self.queue:
            return self.queue[-1]
        return -1
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0
        

    def isFull(self):
        """
        :rtype: bool
        """
        return len(self.queue) == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()