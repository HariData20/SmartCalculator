from collections import deque
n = int(input())
operation = deque()
for _ in range(n):
    input_operation = input().split(' ')
    if input_operation[0] == 'ISSUE':
        operation.append(input_operation[1])
    elif input_operation[0] == 'SOLVED':
        operation.popleft()
        # operation.append(input_operation[1]) if input_operation[0] == 'PUSH' else stack.pop()
print("\n".join([str(operation.popleft()) for _ in range(len(operation))]))
