def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


def even_valued_sequence(seq):
    for i in seq:
        if i % 2 != 0:
            yield i


def under_four_million(seq):
    for i in seq:
        if i > 4000000:
            break
        yield i

# The answer is 4613732
print sum(even_valued_sequence(under_four_million(fib())))