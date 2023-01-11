total, n = int(input()), int(input())
result = 0
for _ in range(n):
    a, b = map(int, input().split()) 
    result += a*b
print("Yes") if result==total else print("No")