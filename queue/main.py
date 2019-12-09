import sys

TYPE = 0
VALUE = 1


class Queue:

    def __init__(self, max_size):

        self._max_size = max_size
        self._front = -1
        self._rear = -1

    def _is_overflow(self):

        if self._front-1 == self._max_size:
            return True

        return False

    def _is_underflow(self):

        if self._rear == self._front:
            return True

        return False


def main():

    lines = sys.stdin.readline()

    for i in range(int(lines)):

        each_line = sys.stdin.readline().split()

        if each_line[TYPE] == 'push':
            print(each_line[VALUE])


if __name__ == "__main__":
    main()
