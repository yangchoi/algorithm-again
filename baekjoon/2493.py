import sys
read = sys.stdin.readline

num = int(read())
num_list = list(map(int, read().split()))

top = [0] * num
stack = []

for i in range(num -1, -1, -1):
    while stack and num_list[stack[-1]] < num_list[i]:
        top[stack.pop()] = i + 1
    stack.append(i)

print(" ".join(map(str, top)))