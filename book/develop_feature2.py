import math
from collections import deque

def solution(progresses, speeds):
    schedules = deque([])
    for idx, progress in enumerate(progresses):
        schedules.append(math.ceil((100 - progress) / speeds[idx]))

    answer = []
    while schedules:
        task = schedules.popleft()
        count = 1
        while schedules and task >= schedules[0]:
            count += 1
            schedules.popleft()
        answer.append(count)

    return answer


