def largest_primefactors(x):
    prime_factors = []
    i = 2
    while x > 1:
        if x % i == 0:
            x = x / i
            prime_factors.append(i)
        else:
            i += 1
    return max(prime_factors)


LargestPrimeFactor = largest_primefactors(600851475143)

# The correct answer is 6857
print LargestPrimeFactor

