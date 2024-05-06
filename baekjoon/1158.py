from collections import deque
import sys
read = sys.stdin.readline

n, k = map(int, read().split())
# n = 7, k = 3
# 1부터 n+1 까지 번호를 deque에 추가
# deque([1, 2, 3, 4, 5, 6, 7])
queue = deque(range(1, n + 1))

# popleft()를 사용해서 요소를 제거하되,
# 요소를 제거하기 전 k-1만큼의 deque 요소들을 오른쪽으로 이동시켜야한다.
result = []
while queue:
    # k-1 만큼 왼쪽으로 회전
    queue.rotate(-(k-1))
    # list.rotate(n) list의 모든 요소들을 오른쪽으로 n 만큼 이동
    # queue.rotate(-(k-1)) 는 k-1 만큼 왼쪽으로 이동
    result.append(queue.popleft())

print(f"<{', '.join(map(str, result))}>")





