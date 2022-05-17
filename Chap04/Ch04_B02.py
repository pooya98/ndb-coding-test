# [Chap04 Implementation] 실전 2. 게임 개발

N, M = map(int, input().split())
A, B, d = map(int, input().split())

field = []
for _ in range(N):
    row = list(map(int, input().split()))
    field.append(row)


move_count = 0
move_types = [(-1, 0), (0, 1), (1, 0), (0, -1)]


field[A][B] = 2
move_count += 1

while True:
    for i in range(1, 5):
        change_flag = False
        cur_d = (d - i) % 4

        next_x = A + move_types[cur_d][0]
        next_y = B + move_types[cur_d][1]

        if (0 <= next_x < N) and (0 <= next_y < M) and field[next_x][next_y] == 0:
            A = next_x
            B = next_y
            field[A][B] = 2

            move_count += 1
            d = cur_d
            change_flag = True
            break
            
        else:
            pass

    if change_flag == False:
        next_x = A - move_types[d][0]
        next_y = B - move_types[d][1]

        if (0 <= next_x < N) and (0 <= next_y < M) and field[next_x][next_y] != 1:
                A = next_x
                B = next_y 

        else:
            break

print(move_count)
    

