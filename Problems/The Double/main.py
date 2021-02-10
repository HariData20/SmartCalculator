# put your python code here
import string

double_alphabet = {i: i * 2 for i in string.ascii_lowercase}
"""
Other solutions
double_alphabet = {key: key + key for key in string.ascii_letters.lower()}
double_alphabet = {val: f"{val}{val}" for val in list(ascii_lowercase)}
list comprehension
print(sum(meal['kcal'] for meal in meals))

"""
some_iterable =['Great', 'loves', 'too', 'must', 'be', 'endured.']
new_dict = {ele.upper(): ele.lower() for ele in some_iterable}
