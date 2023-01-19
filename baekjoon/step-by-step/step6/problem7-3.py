def numbers(n):
    return int(n[::-1])
a, b = map(numbers, input().split())
[print(a) if a>b else print(b)]