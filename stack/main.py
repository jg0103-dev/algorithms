import sys
from stack.bj_stack import Stack

t_idx = 0
v_idx = 1
MAX_SIZE = 100000


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