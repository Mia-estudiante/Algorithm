import sys 
input = sys.stdin.readline
print = sys.stdout.write

nlist = [int(input()) for _ in range(9)]
# print(str(max(nlist))+"\n"+str(nlist.index(max(nlist))+1))
print('%d\n%d' % (max(nlist), nlist.index(max(nlist))+1))