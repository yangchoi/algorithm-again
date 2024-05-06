num = int(input())
arr = set([int(input()) for _ in range(num)])
print(sorted(arr, reverse=True))
