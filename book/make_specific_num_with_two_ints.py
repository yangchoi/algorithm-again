def solution(arr, target):
    for i in arr:
        if target - i in arr:
            return True
    return False
