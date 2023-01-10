dice = [1,2,3,4,5,6]
values = list(map(int, input().split()))
prize = 0
for d in dice:
    num = values.count(d)
    if num<=1:
        continue
    elif num==2:
        prize = 1000+d*100
        break
    else:
        prize = 10000+d*1000
        break
else:
    prize = max(values)*100 
print(prize)