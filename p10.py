def sieve_of_erathosthenes(n):
    primes=[]
    for i in range(n+1):
        primes.append(i)
    primes[0]=0
    primes[1]=0 #0 n 1 cannot be primes

    p=2
    while p*p <= n:
        if p != 0:
            for k in range(p*2, n+1, p): #multiplication is repeated addition
                primes[k] = 0
        p+=1
    only_primes =[]

    for i in primes:
        if i != 0:
            only_primes.append(i)

    return only_primes

#sum of primes
def sum_of_primes_upto(n):
    sum = 0
    for i in sieve_of_erathosthenes(n):
        sum+=i
    return sum

print(sum_of_primes_upto(2000000))
