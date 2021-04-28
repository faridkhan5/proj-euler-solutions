#Longest Collatz sequence
#Which starting number, under one million, produces the longest chain?

store = {1:1}
def collatz(n):
    if n not in store:
        if n%2==0:
            store[n] = collatz(n/2) +1
        else:
            store[n] = collatz((n*3 +1)/2) +2 #reduce time by half
    return store[n]

def longest_collatz_no_lessthan(n):
    longest_chain = 0
    nr_for_chain = 0
    for i in range(1,n):
        length = collatz(i)
        if length > longest_chain:
            longest_chain = length
            nr_for_chain = i
    return nr_for_chain

print(longest_collatz_no_lessthan(1000000))
