import sys
input = sys.stdin.readline
print = sys.stdout.write

n, x = map(int, input().split())
num = input().split()
# num = list(map(int, input().split()))

for n in num:
    if x<=int(n): 
        continue
    print(n+" ") 
