N = int(input())
data = list(map(int, input().split()))

result = 0
count = 0

for i in range(N):
    count += 1
    if data[i] <= count:
        result += 1
        count = 0
print(result)