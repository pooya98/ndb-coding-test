def dfs(graph, v, visited):
    stack = [v]
    visited[v] = True
    print(v, end = ' ')

    while len(stack) > 0:
        current = stack[-1]

        for i in graph[current]:
            if not visited[i]:
                stack.append(i)
                visited[i] = True
                print(i, end = ' ')
                break

        if current == stack[-1]:
            stack.pop()


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

dfs(graph, 1, visited)