# the object_list has already been defined
# write your code here

from collections.abc import Hashable
from collections import Counter
# object_list = [1, 397, 27468, -95, 1309, 397, -539874, -240767, -95, 397]
testing_list = [x for x in object_list if isinstance(x, Hashable)]
count_elements = Counter(testing_list)
max_hash = 0
for _, value in count_elements.items():
    if value > 1:
        max_hash += value
print(max_hash)

"""
Using Dictionary
new_dict = {}

for obj in object_list:
    if isinstance(obj, Hashable):
        if obj in new_dict.keys():
            new_dict[obj] += 1
        else:
            new_dict[obj] = 1

repeat = 0
for val in new_dict.values():
    if val > 1:
        repeat += val

print(repeat)


using list
common_total = 0
hashes_list = [obj for obj in object_list if isinstance(obj, Hashable)]

for obj in set(hashes_list):
    if hashes_list.count(obj) > 1:
        common_total += hashes_list.count(obj)

print(common_total)


Logically correct But can use instance of method

counter = 0

for z in object_list:
    try:
        if [hash(x) for x in object_list].count(hash(z)) > 1:
            counter += 1
    except TypeError:
        continue
print(counter)


"""