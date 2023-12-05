from sys import stdin
read = stdin.readline

count = int(read())
coordinate_list = []
for _ in range(count):
	coordinate_list.append(tuple(int(s) for s in read().split()))
	# python comprehension
coordinate_list.sort()

# for coordinate in coordinate_list:
# 	print(f'{coordinate[0]} {coordinate[1]}')
# 	print(*coordinate) # list, tuple 풀어줌, dictionary 는 **
# 						# arbitrary

ans = '\n'.join(f'{a} {b}' for a, b in coordinate_list)
print(ans)
