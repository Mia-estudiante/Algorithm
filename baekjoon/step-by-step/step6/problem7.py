def numbers(n):
    result = ''
    while n>0:
        a=n%10
        n//=10
        result+=str(a)
    return int(result)

a, b = map(int, input().split())
a, b= numbers(a), numbers(b)
print(a) if a>b else print(b)
