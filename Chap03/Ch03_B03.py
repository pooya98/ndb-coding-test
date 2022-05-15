# [Chap03 Greedy] 실전 3. 1이 되 때까지

from math import remainder
import re


N, K = map(int, input().split())
calculation_count = 0

while N != 1:
    quotient = N // K
    remainder = N % K
    if quotient >= 1:
        calculation_count += remainder + 1
        N = quotient
    else:
        calculation_count += (remainder - 1)
        N = 1

print(calculation_count)