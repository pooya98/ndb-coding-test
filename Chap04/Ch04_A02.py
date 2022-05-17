# [Chap04 Implementation] 예제 4-2. 시각

N = int(input())
count = 0

for i in range(0, N + 1):
    if i % 10 == 3:
        count += 3600
    else:
        count += 105 * 15

print(count)


# 3중 for문 사용한 코드

# N = int(input())
# count = 0

# for hour in range(N + 1):
#     for min in range(60):
#         for sec in range(60):
#             if '3' in str(hour) + str(min) + str(sec):
#                 count += 1

# print(count)