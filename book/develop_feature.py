import math
from collections import deque


def solution(progresses, speeds):
    answer = []
    # 일단 각 task 들이 며칠 후에 끝날지는 구할 수 있을 것 같다
    # 첫번째 93은 100까지 7이 남았고 speeds는 1이니까 7일
    # 두번째 30은 100까지 70이 남았고 speeds는 30이니까 math.ceil(70/30) 하면 3일
    # 세번째 55는 100까지 45가 남았고 speeds는 5니까 match.ceil(45/5) 하면 9일

    # 여기서 첫번째 작업은 7일이고, 이것보다 작은 값은 3밖에 없으니 함께 2가 되고 남은 하나는 본인과 같거나 큰 것이 없으니 1
    days = deque([])
    for idx, p in enumerate(progresses):
        result = (100 - p) / speeds[idx]
        days.append(math.ceil(result))

    # days가 존재할 때까지 계속한다
    # 우선 days[i] 는 popleft 를 하고
    # days를 돌면서 days[i] 보다 작거나 같은 것을 찾는다
    # 찾으면 +1, 못찾으면 0

    while days:
        current_day = days.popleft()
        count = 1

        while days and current_day >= days[0]:
            days.popleft()
            count += 1

        answer.append(count)

    return answer