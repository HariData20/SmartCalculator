n = int(input())
operation = []
popped = []
for _ in range(n):
    input_operation = input().split(' ', 1)
    '''
    if input_operation[0] == 'BUY':
        operation.append(input_operation[1])
    elif input_operation[0] == 'READ':
        popped.append(operation.pop())
        '''
    operation.append(input_operation[1]) if input_operation[0] == 'BUY' else popped.append(operation.pop())
print("\n".join(popped))
