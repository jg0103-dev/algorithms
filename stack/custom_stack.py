

class Stack:

    def __init__(self, max_size):
        self._top = -1
        self._max_size = max_size
        self._stack_arr = [0 for _ in range(self._max_size)]

    def _is_overflow(self):

        if self._top+1 >= self._max_size:
            return True
        else:
            return False

    def _is_underflow(self):

        if self._top < 0:
            return True
        else:
            return False

    def push(self, value):

        if self._is_overflow():
            return

        self._top += 1
        self._stack_arr[self._top] = value

    def pop(self):

        if self._is_underflow():
            return -1

        out_val = self._stack_arr[self._top]
        self._top -= 1

        return out_val

    def size(self):
        return self._top+1

    def empty(self):
        if self.size() > 0:
            return 0
        else:
            return 1

    def top(self):
        if self._is_underflow():
            return -1

        return self._stack_arr[self._top]