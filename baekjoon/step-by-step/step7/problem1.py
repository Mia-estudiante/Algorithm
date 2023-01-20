a, b, c = map(int,input().split())
# result=1

if b>=c:
    # result = -1
    print(-1)
else:
    # result = a//(c-b)+1
    print(a//(c-b)+1)
    # while(c*result <= a+b*result):
    #     result+=1
    
# print(result)