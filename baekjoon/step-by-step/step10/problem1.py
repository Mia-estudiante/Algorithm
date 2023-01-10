n = int(input())
nlist = [int(input()) for _ in range(n)]

'''
선택 정렬
1) 최소값 탐색
2) 첫번째 원소와 비교 후, 삽입
'''
for i in range(n):
    sub = nlist[i:] 
    minv = min(sub)
    minidx = nlist.index(minv)

    nlist[i], nlist[minidx] = minv, nlist[i]

for n in nlist: print(n) 


    