#1. 데이터 입력받기
N, K = map(int, input().split())
coins = list()

for _ in range(N):
    coins.append(int(input()))

#2. 문제 풀기
result = 0
coins.reverse()
while K!=0:
    for coin in coins:
        value = K//coin
        if K//coin == 0:
            continue
        result += value
        K %= coin

print(result) 

'''
1) 역순 방법 3가지 정도 
    - reversed는 느리다.
'''