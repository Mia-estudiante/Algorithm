board = list()
for i in range(9):
    board.append(list(map(int, input().split())))

result = -1 #주의
row = 0
for b in board:
    row+=1
    if result>=max(b): continue
    resultrow, index, result = row, b.index(max(b)), max(b)
print(result)
print(resultrow, index+1)
