

def primeFactors(n):
    """
    (int) --> list(int)
    Returns the prime factors of a number n

    >>>primeFactors(10)
    [2,5]
    >>primeFactors(12)
    [2,2,3]
    """

    factors = []
    d = 2
    while n >= d:
        if n % d == 0:
            factors.append(d)
            n = n/d
            d = 2
        else: d = d+1
    return factors



if __name__ == '__main__':
    print primeFactors(600851475143)
