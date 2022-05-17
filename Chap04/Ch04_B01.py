# [Chap04 Implementation] 실전 1. 왕실의 나이트 

cur_location = input()
x, y = ord(cur_location[0]) - 96, int(cur_location[1])
count = 0

if 0 < x - 2:
    if 0 < y - 1:
        count += 1
    
    if y + 1 < 9:
        count += 1

if x + 2 < 9:
    if 0 < y - 1:
        count += 1
    
    if y + 1 < 9:
        count += 1

if 0 < y - 2:
    if 0 < x - 1:
        count += 1

    if x + 1 < 9:
        count += 1

if y + 2 < 9:
    if 0 < x - 1:
        count += 1

    if x + 1 < 9:
        count += 1

print(count)


# 답안 예시 (이게 더 나음)

# input_data = input()
# x = int(ord(input_data[0])) - int(ord('a')) + 1
# y = int(input_data[1])
# count = 0

# steps = [(-1, -2), (1, -2), (-2, -1), (2, -1), (-2, 1), (2, 1), (-1, 2), (1, 2)]

# for (x_move, y_move) in steps:
#     next_x = x + x_move
#     next_y = y + y_move

#     if (1 <= next_x <= 8) and (1 <= next_y <= 8):
#         count += 1

# print(count)