def multiples3or5():
        for i in xrange(1000):
            if not i % 3 or not i % 5:
                yield i

print sum(multiples3or5())