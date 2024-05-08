import math


def solution(slice, n):
  # n명이 최소 1조각 이상 피자를 먹으려 할 때 최소 몇 판이 필요?
  # > 피자 ceil(n/slice) 판 필요
    return math.ceil(n/slice)
