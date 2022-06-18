N, M = map(int, input().split())

rice_cakes = list(map(int, input().split()))
rice_cakes.sort()
array = []

count = 1
sum = 0
max_height = 0
step = 0
cur_sum = 0

for i in range(N - 1, 0, -1):
    if rice_cakes[i] != rice_cakes[i - 1]:
        sum += count * (rice_cakes[i] - rice_cakes[i - 1])
        array.append((sum, rice_cakes[i - 1], count))
    
    count += 1

sum += (count * rice_cakes[0])
array.append((sum, 0, count))

for i in range(len(array)):
    if(array[i][0] >= M):
        cur_sum = array[i][0]
        max_height = array[i][1]
        step = array[i][2]
        break

max_height += ((cur_sum - M) // step)

print(max_height)



