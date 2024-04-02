from collections import deque
import sys

deq = deque()
n = int(sys.stdin.readline())
for _ in range(n):
    command = sys.stdin.readline().rstrip()
    if len(command) > 1:
        if command[0] == '1':
            deq.appendleft(int(command[2:]))

        else:
            deq.append(int(command[2:]))

    elif command == '3':
        print(-1 if len(deq)==0 else deq.popleft())

    elif command == '4':
        print(-1 if len(deq)==0 else deq.pop())

    elif command == '5':
        print(len(deq))

    elif command == '6':
        print(1 if len(deq)==0 else 0)

    elif command == '7':
        print(-1 if len(deq)==0 else deq[0])

    else:
        print(-1 if len(deq)==0 else deq[-1])