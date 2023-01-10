h, m = map(int, input().split())
time = int(input())

hour = h*60+m+time
h = hour//60
m = hour%60

print(h-24, m) if h>=24 else print(h, m)