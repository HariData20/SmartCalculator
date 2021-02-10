# read sample.txt and print the number of lines
my_file = open('sample.txt', 'r')
"""
count = 0
for _ in my_file:
    count += 1
print(count)
"""
my_file.close()
a = [1, 2, 3]
b = a
print(b)
print(id(a))
print(id(b))
a[1] = 10
# and here?
print(b)
b[0] = 20
# what about now?
print(b)
a = [5, 6]
print(id(a))
print(id(b))
# it is the last time, we promise. The value of b?
print(b)