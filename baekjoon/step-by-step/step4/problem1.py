import sys

input = sys.stdin.readline
print = sys.stdout.write

int(input())
num = list(map(int, input().split()))
v = int(input())

print(str(num.count(v)))
