for _ in range(int(input())):
    h, w, n = map(int, input().split())
    if n%h: yy, xx = n%h, n//h+1
    else: yy, xx = h, n//h
    print(f'{yy}0{xx}') if len(str(xx))==1 else print(f'{yy}{xx}')

'''
1. 손님 번호가 h의 배수인 경우도 고려
2. 문자열이 아닌 숫자 형태로 출력하는 것이 더 빠를 듯
'''