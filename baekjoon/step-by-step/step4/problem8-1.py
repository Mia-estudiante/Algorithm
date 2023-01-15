for _ in range(int(input())):
    ox = list(input())
    result = 0
    value = 1
    for i in ox:
        if i=='O':
            result+=value
            value+=1
        else: value=1
    print(result)