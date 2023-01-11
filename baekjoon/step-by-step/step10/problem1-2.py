n = int(input())
nlist = [int(input()) for _ in range(n)]

for i in range(n-1):
    minidx = i
    for j in range(i, n):
        if nlist[j]>nlist[minidx]:
            continue
        minidx = j
    nlist[minidx], nlist[i] = nlist[i], nlist[minidx]

for n in nlist:
    print(n)