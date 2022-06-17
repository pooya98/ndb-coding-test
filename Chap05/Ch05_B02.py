from collections import deque


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(maze, startX, startY, endX, endY):
    result = 0

    q = deque()
    q.append((startX, startY, 1))

    while q:
        (curX, curY, step_count) = q.popleft()
        maze[curX][curY] = 2

        if(curX == endX and curY == endY):
            result = step_count
            break

        for i in range(4):
            nextX = curX + dx[i]
            nextY = curY + dy[i]

            if(nextX < 0 or nextX > endX or nextY < 0 or nextY > endY):
                continue
            else:
                if maze[nextX][nextY] == 1:
                    q.append((nextX, nextY, step_count + 1))

    
    return result
    



N, M = map(int, input().split())

maze = []

for _ in range(N):
    maze.append(list(map(int, input())))

print(bfs(maze, 0, 0, N - 1, M - 1))
