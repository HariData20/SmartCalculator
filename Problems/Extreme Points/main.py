# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())
#test_dict = {"a": 43, "b": 1233, "c": 8}
# Work with the 'test_dict'
print('min:', min(test_dict, key=test_dict.get))
print('max:', max(test_dict, key=test_dict.get))

"""
other solutions
mini = [x for x, y in test_dict.items() if int(y) == min(test_dict.values())]
maxi = [x for x, y in test_dict.items() if int(y) == max(test_dict.values())]
"""