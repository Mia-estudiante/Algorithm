def sum_numbers(n):
    result = 0
    while n>0:
        result+=n%10
        n//=10
    return result
input()
# print(sum_numbers(int(input())))
print(sum(list(map(int, input()))))