import sys
input = sys.stdin.readline
print = sys.stdout.write

input()
num = list(map(int, input().split()))
print(str(min(num))+" "+str(max(num)))