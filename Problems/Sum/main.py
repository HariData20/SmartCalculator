# read sums.txt
my_file = open('sums.txt', 'r')
for line in my_file:
    print(sum(int(x) for x in line.split()))
my_file.close()
