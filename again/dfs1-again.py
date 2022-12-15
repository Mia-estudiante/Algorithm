def dfs(start, visited, stack, graph):
    #1. 방문표시
    visited[start] = True
    print(start, end=' ')

    #2. 방문하고 있는 노드의 인접노드들 확인
    for node in graph[start]:
        if visited[node]: #2-1. 방문했는지 확인
            continue
        stack.append(node)
        dfs(node, visited, stack, graph)

#1. 그래프 만들기
graph = [[],
        [2, 3],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7]]

#2. 방문확인
visited = [False]*(len(graph))

#3. 스택 생성
stack = []

#4. dfs 수행
dfs(1, visited, stack, graph)
print(stack)

'''
방문하면서 방문 표시
'''