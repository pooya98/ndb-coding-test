# [Chap03 Greedy] 예제 3-1. 거스름돈

change = int(input())
coin_types = [500, 100, 50, 10]
coin_count = 0

for coin_type in coin_types:
    coin_count += (change // coin_type)
    change %= coin_type

print(coin_count)
    
