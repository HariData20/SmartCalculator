from collections import deque

n = int(input())
operation = deque()
popped = []
for _ in range(n):
    input_operation = input().split(' ', 1)

    if input_operation[0] == 'READY':
        operation.append(input_operation[1])
    elif input_operation[0] == 'EXTRA':
        operation.append(operation.popleft())
    elif input_operation[0] == 'PASSED':
        popped.append(operation.popleft())

    #operation.append(input_operation[1]) if input_operation[0] == 'BUY' else popped.append(operation.pop())
print("\n".join(popped))
