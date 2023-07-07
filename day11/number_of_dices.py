import math


def solution(box, n):
    # prod: () 안에 있는 모든 iterable 요소들의 곱을 구한다
    # box 안에 있는 모든 값 v들을 n으로 나눈 몫을 모두 곱하는 값을 구한다.
    return math.prod(map(lambda v: v//n, box))
