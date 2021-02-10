n = int(input())
operation = []
for _ in range(n):
    input_operation = input().split(' ')
    if input_operation[0] == 'PUSH':
        operation.append(input_operation[1])
    elif input_operation[0] == 'POP':
        operation.pop()
        # operation.append(input_operation[1]) if input_operation[0] == 'PUSH' else stack.pop()
print("\n".join([str(operation.pop()) for _ in range(len(operation))]))


