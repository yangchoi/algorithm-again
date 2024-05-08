def solution(n):
    # 합성수 : 약수의 개수가 세개 이상인 수
    answer = 0
    for i in range(1, n+1):
        count = 0  # 약수의 개수
        for j in range(1, i+1):
            # 약수: 자기 자신보다 작거나 같은 수
            if i % j == 0:
                # i가 j로 나누어지면 j는 i의 약수
                count += 1
        if count >= 3:
            # count가 3보다 크거나 같으면 약수의 개수가 3개 이상이므로 합성수
            answer += 1
    return answer
