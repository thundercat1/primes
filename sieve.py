import sys
import time

def erat(n, option=1):
    """
    Takes an integer n and returns a list of prime numbers up to and including n.
    Supports a second optional argument of int either 1 or 2. If 2 is specified,
    returns a list of booleans indicating whether a given index is prime. 

    Computing the primes implements the Sieve of Eratosthenes algorithm

    (int, int(optional)) --> list(int)
    >>>erat(10)
    [1,2,3,5,7]

    >>>erat(19)
    [1,2,3,5,7,11,13,17,19]

    >>>erat(10,2)
    [1,2,3,5,7,11,13,17,19,23]
    """

    assert n > 3, 'Use this sieve to find more than three primes. You asked for ' + str(n)
                      
    if option==1:
        
        #Initialize array for sieve. At this point, all odd values are candidates
        #Treat indices as odd values starting at 1
        #[0,1,2,3,4,5,6] --> [1,3,5,7,9,11,13]
        #If we're eliminating 
        candidates = [True]*(1 + n/2)
        
        #Begin by looking for multiples of three to eliminate
        prime = 3
        primes = [1,2,3]

        while prime * prime <= n:
            #Start with the third multiple (second multiple is even so it's already been eliminated)
            for eliminate in range(prime*prime,n,prime*2): 
                #eliminate all odd multiples of the current prime, beginning with its square
                candidates[eliminate/2] = False

            #Increment prime to the next True value in candidate array:
            prime += 2
            while not candidates[prime/2]:
                #keep looking for the next prime number
                prime += 2
            primes.append(prime)

        prime = primes[len(primes)-1] + 2
        while  prime <= n:
            if candidates[prime/2]:
                primes.append(prime)
            prime += 2

        return primes


    elif option == 2:
        #Initialize array for sieve. At this point, all values are candidates
        candidates = [True]*(n+1)
        candidates[0] = False
        
        i=4
        while i <= n:
            candidates[i] = False
            i += 2

        #Begin by looking for multiples of two to eliminate
        #prime = 2
        prime = 3
        while prime * prime <= n:
            #Start with the third multiple (second multiple is even so it's already been eliminated)
            eliminate = prime * prime
            while eliminate <= n:
                #eliminate all odd multiples of the current prime, beginning with its square
                candidates[eliminate] = False
                eliminate += 2*prime

            #Increment prime to the next True value in candidate array:
            prime += 1
            while not candidates[prime]:
                #keep looking for the next prime number
                prime += 1

    return candidates



if __name__ == '__main__':
    print 'Primes to 20, called with option 2 are ' + str(erat(20,2))
    n = 1000000
    print 'Testing run time with option 2 and n = ' + str(n)
    startTime = time.time()
    erat(n,2)
    stopTime = time.time()
    print 'Run time: ' + str(stopTime - startTime)
    

