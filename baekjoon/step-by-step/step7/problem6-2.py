import sys
input = sys.stdin.readline
print = sys.stdout.write

for _ in range(int(input())):
    k, n = int(input()), int(input())
    people = [ i for i in range(1, n+1) ]
    for _ in range(k):
        for i in range(1, n):
            people[i] += people[i-1]
    print(f'{people[-1]}\n')