from sys import stdin
import itertools

read = stdin.readline
n = int(read())
k = int(read())

nums = []
for i in range(n):
    num = read().strip()
    nums.append(num)

num_set = set()
# intertools.permutations: k 조합의 순열 (순서 신경 쓸 때)
# intertools.combination: 순서가 상관없는 조합을 쓸 때
for j in itertools.permutations(nums, k):
    num_set.add(''.join(j))

print(len(num_set))
