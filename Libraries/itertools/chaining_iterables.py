import itertools


iterable_1 = ['a', 'b', 'c']
iterable_2 = range(6)
iterable_3 = {9, 6}

for item in itertools.chain(iterable_1, iterable_2, iterable_3):
    print(item)

# way to flatten
list(itertools.chain.from_iterable([[1, 2, 3], [4, 5, 6]]))