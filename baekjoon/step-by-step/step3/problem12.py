ori = input()
if len(ori)==1: ori = '0'+ori
n = list(ori)
result = 0
while True:
    a, b = n[0], n[1]
    c = str(int(a)+int(b))
    n = b+c[-1:]
    result +=1

    if n==ori: break 
    else: n = list(n)
    
print(result)