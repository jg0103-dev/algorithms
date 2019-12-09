

class Queue:

    def __init__(self, max_size):

        self._max_size = max_size
        self._front = 0
        self._rear = 0
        self._arr = [0 for _ in range(self._max_size)]

    def _is_underflow(self):

        if self._rear >= self._front:
            return True

        return False

    def push(self, data):
        self._arr[self._front] = data
        self._front += 1

    def pop(self):
        if self._is_underflow():
            return -1

        res = self._arr[self._rear]
        self._rear += 1

        return res

    def size(self):
        res = (self._front-self._rear)
        return res

    def front(self):
        if self._is_underflow():
            return -1

        return self._arr[self._front-1]

    def empty(self):
        if self._is_underflow():
            return 1

        return 0

    def back(self):
        if self._is_underflow():
            return -1

        return self._arr[self._rear]