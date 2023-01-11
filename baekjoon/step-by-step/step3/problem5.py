import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(str(a+b)+'\n')