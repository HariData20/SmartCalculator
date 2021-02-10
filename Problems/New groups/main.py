# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here
strength = []
no_of_classes = int(input())
classes = dict.fromkeys(groups)
for i in range(no_of_classes):
    classes[groups[i]] = int(input())
print(classes)
