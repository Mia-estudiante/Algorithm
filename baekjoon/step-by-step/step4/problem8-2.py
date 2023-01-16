import sys

input = sys.stdin.readline

for _ in range(int(input())):
    result = 0
    os = input().rstrip("\n").split("X")
    for o in os:
        if not o: continue
        result+=sum(range(1, len(o)+1))
    sys.stdout.write(f"{result}\n") 