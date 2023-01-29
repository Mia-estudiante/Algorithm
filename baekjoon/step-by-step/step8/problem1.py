def is_prime_number(n):
    n = int(n)
    if n==1: return False
    for i in range(2, n):
        if n%i: continue
        return False
    return True

input()
n = list(map(is_prime_number, input().split())).count(True)
print(n)