iris = {}


def add_iris(id_n, species, petal_length, petal_width, **kwargs):
    e = {"species": species, "petal_length": petal_length, "petal_width": petal_width, **kwargs}
    iris.update({id_n: e})



"""
Other solutions:

    item = {'species': species, 'petal_length': petal_length, 'petal_width': petal_width}
    for key, value in kwargs.items():
        item[key] = value
    iris[id_n] = item
    
        inter_dict = {id_n: {"species": species, "petal_length": float(petal_length), "petal_width": float(petal_width)}}
    for parameters, values in other_details.items():
        inter_dict[id_n][parameters] = values
    iris.update(inter_dict)
"""