# [Chap03 Greedy] 실전 1. 큰 수의 법칙

N, M, K = map(int, input().split(" "))

max_sum = 0

int_list = list(map(int, input().split()))
int_list.sort(reverse=True)

cycle = M // (K + 1)

max_sum += cycle * (int_list[0] * K + int_list[1])
max_sum += (M % (K + 1)) * int_list[0]

print(max_sum)

