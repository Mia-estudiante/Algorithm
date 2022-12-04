n = int(input())
array = list(map(int, input().split()))

# 앞에서 계산된 값들을 저장하기 위한 DP 테이블 초기화
d = [0] * 100 # 100인 이유는..n의 최대값이 100이기에

d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+array[i])

print(d[n-1])