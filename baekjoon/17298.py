import sys
input = sys.stdin.readline

num = int(input())
num_list = list(map(int, input().split()))

next_bigger = [-1] * num
stack = []

for i in range(num):
    while stack and num_list[stack[-1]] < num_list[i]:
        next_bigger[stack.pop()] = num_list[i]
    stack.append(i)

print(" ".join(map(str, next_bigger)))