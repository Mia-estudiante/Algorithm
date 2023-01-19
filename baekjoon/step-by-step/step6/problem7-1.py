def numbers(n):
    result = ''
    while n>0:
        a=n%10
        n//=10
        result+=str(a)
    return int(result)

a, b = map(numbers, input().split())
a, b= numbers(a), numbers(b)
print(a) if a>b else print(b)

'''
map 함수 내 함수를 넣든 안 넣든, 
일단 문자열을 다루는 것보다 "숫자"를 다루는 것이 속도 면에서 좋다
'''
