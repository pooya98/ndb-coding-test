# [Chap03 Greedy] 실전 2. 숫자 카드 게임

N, M = map(int, input().split(" "))
board = []
max = 0

for i in range(1, N + 1):
    board.append(list(map(int, input().split(" "))))

for row in board:
    row_max = min(row)
    if max < row_max:
        max = row_max

print(max)