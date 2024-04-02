from collections import deque
import sys

deq = deque()
n = int(sys.stdin.readline())
size = 0
for _ in range(n):
    command = sys.stdin.readline().rstrip()
    if len(command) > 1:
        if command[0] == '1':
            deq.appendleft(int(command[2:]))
            size += 1

        else:
            deq.append(int(command[2:]))
            size += 1

    elif command == '3':
        if size==0:
            print(-1)
        else:
            print(deq.popleft())
            size -= 1

    elif command == '4':
        if size==0:
            print(-1) 
        else:
            print(deq.pop())
            size -= 1

    elif command == '5':
        print(size)

    elif command == '6':
        print(1 if size==0 else 0)

    elif command == '7':
        print(-1 if size==0 else deq[0])

    else:
        print(-1 if size==0 else deq[-1])