h, m = map(int, input().split())

h*=60
h+=m
h-=45

print(23, 60+h) if h<0 else print(h//60, h%60)