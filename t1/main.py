import sys
from t1.bj_queue import Queue

t_idx = 0
v_idx = 1
MAX_SIZE = 10000


def main():

    queue = Queue(MAX_SIZE)

    lines = sys.stdin.readline()

    for i in range(int(lines)):

        each_line = sys.stdin.readline().split()
        q_type = each_line[t_idx]

        if q_type == 'push':
            queue.push(each_line[v_idx])

        if q_type == 'pop':
            print(queue.pop())

        if q_type == 'size':
            print(queue.size())

        if q_type == 'empty':
            print(queue.empty())

        if q_type == 'front':
            print(queue.back())

        if q_type == 'back':
            print(queue.front())


if __name__ == "__main__":
    main()
