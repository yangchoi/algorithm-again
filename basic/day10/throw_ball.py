def solution(numbers, k):
    answer = 0
    if len(numbers) < k * 2:
        # k번을 두칸씩 건너뛰어야하기 때문에 위와 같은 상황에서는 numbers를 확장시켜주어야함
        numbers = numbers * ((k*2) // len(numbers) + 1)
        # numbers * 1를 하면 원래 리스트와 같아지기 때문에 +1을 해주어 확장시켜준다.

    answer = numbers[2*(k-1)]
    # k번째 공을 던지는 사람을 찾기 위해 numbers의 2(k-1) 번째 요소를 찾아준다.
    # 2*k를 하면 k번째 공을 받는 사람이 되기 때문에 k-1해주어야 k번째 공을 던지는 사람을 찾을 수 있다.
    return answer
