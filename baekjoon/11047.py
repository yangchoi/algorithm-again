from sys import stdin
read = stdin.readline

count, price = [int(s) for s in read().split()]
coin_list = [int(input()) for _ in range(count)]
coin_count = 0
while price > 0 and (coin := coin_list.pop()):
	coin_count += price // coin
	price -= coin * (price // coin)

print(coin_count)
