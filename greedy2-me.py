nums = input()
n1, n2 = int(nums[0]), int(nums[1])
result =0

if((n1==0) | (n2==0)| (n1==1) | (n2==1)): # 괄호하는 거 중요
    result += (n1+n2)
else:
    result = n1*n2
    
for n in nums[2:]:
    n = int(n)
    if n==0:
        continue
    elif n==1:
        result += 1
    else:
        result*=n
print(result)