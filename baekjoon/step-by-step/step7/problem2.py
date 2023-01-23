goal = int(input())

cnt = 0
last = 1 

while(last<goal): #현재 last
    cnt+=1 #현재 cnt
    last+=6*(cnt-1) #현재 last
print(cnt) if goal!=1 else print(1)