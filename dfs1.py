# DFS 메서드
def dfs(graph, v, visited):
    # 1. 현재 노드 방문 처리
    visited[v] = True
    print(v, end=' ') # 방문 순서를 확인하기 위함

    # 2. 현재 방문한 노드와 연결된 노드들을 확인
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 그래프 - 2차원 리스트
graph = [
    [],
    [2,3,8],    #1
    [1,7],      #2
    [1,4,5],    #3
    [3,5],      #4
    [3,4],      #5
    [7],        #6
    [2,6,8],    #7
    [1,7]       #8
]

# 각 노드가 방문된 정보 표현 - 1차원 리스트
visited = [False]*len(graph)

# DFS 함수 호출
dfs(graph, 1, visited)