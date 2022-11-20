def dfs(x, y):
    #1. x, y 범위 확인
    if x<=-1 or y<=-1 or x>=N or y>=M:
        return False
    
    #2. 방문 안 한 노드라면(얼음이 있는 곳이라면)
    if graph[x][y]==0:
        #차례로 상하좌우 확인
        #3. 현재 노드 방문 처리
        graph[x][y]=1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

N, M = map(int, input().split())
result = 0

graph = list()
for _ in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if dfs(i, j):
            result += 1

print(result)