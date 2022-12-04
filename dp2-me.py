x = int(input())
dp = [0] * 30001 # 입력될 수 있는 x의 최대값이 30000이기에

'''
x: 1~30000
연산 1. 1 빼기
연산 2. 2로 나누기
연산 3. 3로 나누기
연산 4. 5로 나누기
'''

# x = 1
dp[1] = 0

for i in range(2, x+1): # x: 2~30000

    # 1. (2, 3, 5)로 나눠지지 않는 경우가 존재    
    dp[i] = dp[i-1]+1
    if i%2==0: 
        dp[i] = min(dp[i//2]+1, dp[i])
    if i%3==0:
        dp[i] = min(dp[i//3]+1, dp[i])
    if i%5==0:
        dp[i] = min(dp[i//5]+1, dp[i])

print(dp[x])

'''
x = 26
1) 26-1 => 25
2) 25 / 5 => 5
3) 5 / 5 => 1 
나눌 수 있으면 나누는 게 좋음
'''