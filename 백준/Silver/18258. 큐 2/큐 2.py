from collections import deque
import sys

queue = deque()
n = int(sys.stdin.readline())
size = 0
for _ in range(n):
    command = sys.stdin.readline().split()
    if len(command) > 1:
        queue.append(int(command[1]))
        size += 1

    elif command[0] == 'pop':
        if size==0:
            print(-1)
        else:
            print(queue.popleft())
            size -= 1

    elif command[0] == 'size':
        print(size)

    elif command[0] == 'empty':
        print(1 if size==0 else 0)

    elif command[0] == 'front':
        print(-1 if size==0 else queue[0])

    elif command[0] == 'back':
        print(-1 if size==0 else queue[-1])