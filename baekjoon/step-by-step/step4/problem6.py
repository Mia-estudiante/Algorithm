import sys

input = sys.stdin.readline
num = [int(input())%42 for _ in range(10)]
print(len(set(num)))