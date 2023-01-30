m=(l:=sum([list(map(int,input().split()))for _ in range(9)],[])).index(a:=max(l))
print(f'{a}\n{m//9+1} {m%9+1}')

'''
1. :=
선언과 동시에 초기화

2. sum(2차원 배열, [])
하나의 list로 만들기
'''