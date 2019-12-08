import sys

t_idx = 0
v_idx = 1
MAX_SIZE = 100000


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


def main():

    lines = sys.stdin.readline()
    lines = int(lines)
    stack = Stack(MAX_SIZE)

    for line in range(lines):
        each_line = sys.stdin.readline().split()
        stack_type = each_line[t_idx]

        if stack_type == 'push':
            stack.push(int(each_line[v_idx]))

        if stack_type == 'pop':
            print(stack.pop())

        if stack_type == 'size':
            print(stack.size())

        if stack_type == 'empty':
            print(stack.empty())

        if stack_type == 'top':
            print(stack.top())


if __name__ == "__main__":
    main()