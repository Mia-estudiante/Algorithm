import sys

input = sys.stdin.readline
print = sys.stdout.write

total = [i+1 for i in range(30)]
done = [int(input()) for _ in range(28)]
result = [x for x in total if x not in done]
result.sort()
print("%d\n%d" % (result[0], result[1]))
