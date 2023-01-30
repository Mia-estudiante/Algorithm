import sys
input = sys.stdin.readline
# print = sys.stdout.write

def is_prime_number(n):
    if n==1: return -1
    for i in range(2, n):
        if n%i: continue
        return -1
    return n

numbers = range(int(input()), int(input())+1)
primes = set(list(map(is_prime_number, numbers)))
if -1 in primes: primes.remove(-1)
print(f'{sum(primes)}\n{min(primes)}') if primes else print(-1)