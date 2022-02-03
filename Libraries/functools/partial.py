import functools

def spam(a, b, c, d):
    ...
    return 0



if __name__ == '__main__':
    p1 = functools.partial(spam, 1, 2, 3)
    # only d argument needs to be specified
    p1(4)
