from collections import deque
import sys
myDeque=deque()

repeat_num=int(sys.stdin.readline())

for i in range(repeat_num):
    num=int(sys.stdin.readline())
    if num==0:
        myDeque.pop()
    else:
        myDeque.append(num)


print(sum(myDeque))
