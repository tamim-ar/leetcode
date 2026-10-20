class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self._next = self.iterator.next() if self.iterator.hasNext() else None

    def peek(self):
        """
        Returns the next element in the array without moving the pointer.
        :rtype: int
        """
        return self._next

    def next(self):
        """
        :rtype: int
        """
        val = self._next
        self._next = self.iterator.next() if self.iterator.hasNext() else None
        return val

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._next is not None