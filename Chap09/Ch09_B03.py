import heapq
INF = int(1e9)
N, M, C = map(int, input().split())

graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M):
    start, end, dist = map(int, input().split())

    graph[start].append((end, dist))

def dijkstra(start):
    q = []

    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        cur_dist, cur_index = heapq.heappop(q)

        if distance[cur_index] < cur_dist:
            continue

        for next_index, next_dist in graph[cur_index]:
            cost = cur_dist + next_dist

            if cost < distance[next_index]:
                distance[next_index] = cost
                heapq.heappush(q, (distance[next_index], next_index))

dijkstra(C)

dest_count = 0
max_time = 0

for i in range(1, N + 1):
    if distance[i] != INF and i != C:
        dest_count += 1

for i in range(1, N + 1):
    if distance[i] != INF and distance[i] > max_time:
        max_time = distance[i]

print(dest_count, max_time)