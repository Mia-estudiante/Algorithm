memo = [0]*100

n = int(input())
food = list(map(int, input().split()))

memo[0] = food[0]
memo[1] = max(food[0], food[1])

for i in range(2, n):
    memo[i] = max(memo[i-1], memo[i-2]+food[i])

print(memo[n-1])