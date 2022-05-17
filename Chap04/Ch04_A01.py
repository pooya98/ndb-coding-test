# [Chap04 Implementation] 예제 4-1. 상하좌우

N = int(input())
move_plan = list(map(str, input().split())) # move_plan = input().split() 으로 가능

x, y = 1, 1


for move in move_plan:
    if move == 'R':
        if y < N:
            y += 1
    
    elif move == 'L':
        if y > 1:
            y -= 1
    
    elif move == 'U':
        if x > 1:
            x -= 1
    
    elif move == 'D':
        if x < N:
            x += 1

print(x, y)