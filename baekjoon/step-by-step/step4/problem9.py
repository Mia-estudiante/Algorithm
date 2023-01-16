import sys
input = sys.stdin.readline
print = sys.stdout.write

for _ in range(int(input())):
    nstd = list(map(int, input().split()))
    n=nstd[0]
    std=nstd[1:]
    avg = sum(std)/n
    
    ext = [x for x in std if x>avg]
    ratio = len(ext)/n * 100
    print(f"{ratio:.3f}%\n")