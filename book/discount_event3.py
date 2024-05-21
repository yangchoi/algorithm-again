from collections import Counter


def solution(want, number, discount):
    answer = 0

    want_dict = dict(zip(want, number))

    for i in range(len(discount) - 9):
        if want_dict == Counter(discount[i:i + 10]):
            answer += 1

    return answer

"""
윈도우 슬라이딩
배열, 리스트 같은 데이터 구조에서 연속된 구간을 탐색하는 방법
특정 크기 윈도우(구간)를 데이터 구조 내에서 이동시키며 필요한 작업 수행 시 사용
윈도우 크기는 고정되며 한 요소씩 이동하며 연속된 구간에 대한 처리 반복
"""

# 예시 최대 연속 부분합 구하기
def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return 'invalid'

    # 첫 윈도우 합 계산
    max_sum = sum(arr[:k])
    current_sum = max_sum

    # 윈도우를 오른쪽으로 이동
    for i in range(k, n):
        current_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, current_sum)

    return max_sum
