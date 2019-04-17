import random

# Store all sample in x; x include lists of list
x = [[] for _ in range(6)]
for i in range(1000):
    x[0].append(random.gauss(2, 0.3))
    x[1].append(random.gauss(2, 0.3))
    x[2].append(random.gauss(-2, 0.3))
    x[3].append(random.gauss(-2, 0.3))
    x[4].append(random.gauss(-2, 0.3))
    x[5].append(random.gauss(3, 0.3))


# Visualize data; feel free to delete or skip this part of code
for i in range(1000):
    print('%s\t%s\t%s' % ('0',x[0][i], x[1][i]))
    print('%s\t%s\t%s' % ('1',x[2][i], x[3][i]))
    print('%s\t%s\t%s' % ('2',x[4][i], x[5][i]))
