import sys
input = sys.stdin.readline
print = sys.stdout.write

def people(floor, n):
    return [sum(floor[0:i+1]) for i in range(n)]

for _ in range(int(input())):
    k, n = int(input()), int(input())
    mem = [[i for i in range(1, n+1)]]
    # for _ in range(k-1):
    #     mem.append([0 for _ in range(n)])

    for i in range(1, k):
        mem.append(people(mem[i-1], n))
    print(f'{sum(mem[k-1])}\n')
