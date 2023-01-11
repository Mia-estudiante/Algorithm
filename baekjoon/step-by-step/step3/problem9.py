import sys
n = int(input())
print = sys.stdout.write
for i in range(1, n+1):
    print(" "*(n-i)+"*"*i+"\n")
    # print("*"*i+"\n")