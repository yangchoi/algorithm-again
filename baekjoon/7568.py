count = int(input())

info = []
for _ in range(count):
	info.append(tuple(int(s) for s in input().split()))

answer = []
for x, y in info:
	rank = 1
	for p, q in info:
		if x < p and y < q:
			rank += 1
	answer.append(rank)

print(*answer)
