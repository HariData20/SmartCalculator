def tallest_people(**heightdict):
    max_height = [x for x,y in sorted(heightdict.items()) if int(y) == max(heightdict.values())]
    for key in max_height:
        print('{} : {}'.format(key, heightdict.get(key)))

'''
other solutions:
def tallest_people(**kwargs):
    for key, value in sorted(kwargs.items()):
        if value == max(kwargs.values()):
            print(f'{key} : {value}')
'''