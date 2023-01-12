ori = int(input())
n = ori
result = 0
while True:
    a, b = n//10, n%10
    n = b*10+(a+b)%10
    result+=1
    if ori!=n: continue
    break
print(result)
