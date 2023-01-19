def numbers(n):
    n = int(n) # 추가
    result = ''
    while n>0:
        a=n%10
        n//=10
        result+=str(a)
    return int(result)

a, b = map(numbers, input().split())
# a, b= numbers(a), numbers(b)
print(a) if a>b else print(b)
