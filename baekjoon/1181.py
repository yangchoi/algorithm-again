count = int(input())
words = sorted(set([(len(i := input()), i) for _ in range(count)]))

for word in words:
	print(word[1])
