from sys import stdin

queue = []

N = int(stdin.readline())

for _ in range(N):
    input_ = stdin.readline().split()
    if input_[0] == 'push':
        queue.append(input_[1])
    elif input_[0] == 'pop':
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    elif input_[0] == 'size':
        print(len(queue))
    elif input_[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif input_[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif input_[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])