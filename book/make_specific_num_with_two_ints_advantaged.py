# arr에서 임의의 원소 x에 대해 x + k = taget이 되는 원소 k가 arr에 있는지 확인
def count_sort(arr, k):
    hashtable = [0] * (k + 1)

    for num in arr:
        # 현재 원소값이 k(target) 이하일 때만 처리
        if num <= k:
            # 현재 원소 값을 인덱스로 해 해당 인덱스 해시 테이블 값을 1로 설정
            hashtable[num] = 1
    return hashtable


def solution(arr, target):
    hashtable = count_sort(arr, target)

    for num in arr:
        complement = target - num
        # target에서 현재 원소를 뺀 값이 해시 테이블에 있는지 확인
        if (
            complement != num
            and 0 <= complement <= target
            and hashtable[complement] == 1
        ):
            return True
    return False
