goal = int(input())

cnt = 1
last = 1 

while(last<goal):
    last+=(cnt+1)
    cnt+=1
a = cnt-(last-goal) #자기위치
b = cnt+1-a
print(f"{b}/{a}") if cnt%2 else print(f"{a}/{b}")