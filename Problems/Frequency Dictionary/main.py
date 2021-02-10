# put your python code here
words = [word.lower() for word in input().split()]
dict_count = {}

for word1 in words:
    count = 0
    for word2 in words:
        if word1 == word2:
            count += 1
    dict_count[word1] = count
for k, v in dict_count.items():
    print(k, v)


"""
Other solutions
Dict comprehension
words = input().lower().split()
for k, v in {word: words.count(word) for word in words}.items():
    print(k, v)

"""