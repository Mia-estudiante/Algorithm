def is_prime_number(n):
    for i in range(2, n):
        if n%i: continue
        return False
    return True

def factorization(n):
    k = 2
    while n>1:
        for i in range(k, n):
            if n%i: continue
            n//=i
            k = i
            print(k)
            break
        if is_prime_number(n):
            print(n)
            break

factorization(int(input()))

'''
n = 1인 경우 고려!
'''