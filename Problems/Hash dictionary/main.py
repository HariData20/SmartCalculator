# create your dictionary here

from collections.abc import Hashable

objects_dict = {}
for x in objects:
    if isinstance(x, Hashable):
        objects_dict[x] = hash(x)

"""
objects_dict = {i: hash(i) for i in objects if isinstance(i, Hashable)}


Exceptions:
objects_dict = {}
for i in objects:
    try:
        objects_dict.update({i: hash(i)})
    except TypeError:
        pass

"""
