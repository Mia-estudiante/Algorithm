import sys
print = sys.stdout.write

for _ in range(int(input())):
    rs = list(input().split())
    for w in rs[1]:
        print(w*int(rs[0]))
    print('\n')