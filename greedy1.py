N, k = map(int, input().split())
result = 0

while True:
    target = (N // k) *k    # N과 가장 가까운 k의 배수
    result += (N - target)  # target까지 1을 빼야 하는 횟수
    N = target              # target(k의 배수)이 된 N
    if N < k:               # 나누기를 할 수 없는 시점 = 1을 빼야 할 시점
        break
    N //= k                 # 나누기
    result+=1               # 나누셈의 횟수

result += (N - 1)           # N=1이 될 때까지 1을 빼야 하는 횟수
print(result)
