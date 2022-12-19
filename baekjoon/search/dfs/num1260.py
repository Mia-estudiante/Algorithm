from collections import deque
import copy 
def bfs(start, graph, visited):
    #1. 방문표시
    queue = deque([start])
    visited[start] = True #
    # print(start, end=' ')
    
    #2. 
    while queue:
        start = queue.popleft()
        print(start, end=' ')
        # visited[start] = True
        for node in graph[start]:
            if not visited[node]: 
                queue.append(node)
                visited[node] = True #
                

def dfs(start, graph, visited):
    #1. 방문표시
    visited[start] = True
    print(start, end=' ')

    #2. 인접노드 확인
    for node in graph[start]:
        if not visited[node]:
            dfs(node, graph, visited)

#1. 데이터 입력받기
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    temp = list(map(int, input().split()))
    graph[temp[0]].append(temp[1])
    graph[temp[1]].append(temp[0])

#2. 데이터 정렬 필요
for g in graph:
    g.sort()

#3. 방문 표시할 리스트 생성
visited1 = [False] * len(graph)
visited2 = copy.deepcopy(visited1)

graph2 = copy.deepcopy(graph)

#3. dfs 수행
dfs(V, graph, visited1)
# print("\n")
bfs(V, graph2, visited2)

# printResult(bfs())
# print(graph)