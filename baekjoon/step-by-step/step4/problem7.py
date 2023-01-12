import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
score = list(map(int, input().split()))
maxs = max(score)
score = [x/maxs*100 for x in score]
print("%f" % (sum(score)/n))