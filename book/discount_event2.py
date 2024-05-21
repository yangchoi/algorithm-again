def solution(want, number, discount):
    want_dict = dict(zip(want, number))

    answer = 0

    # 할인 목록에서 10일 간격 순회
    for i in range(len(discount) - 9):
        discount_10day = {} # i 일 회원가입 시 할인받는 제품 및 개수를 담을 딕셔너리

        # i 일 부터 i + 10일까지 10일 동안의 할인 품목 순회
        for j in range(i, i + 10):
            # 현재 할인 품목이 want_dict 에 있는지 확인
            if discount[j] in want_dict:
                # 현재 할인 품목은 discount_10day에 추가
                discount_10day[discount[j]] = discount_10day.get(discount[j], 0) + 1
                # discount_10day.get(discount[j], 0) 은 현재 품목 개수를 가져오고 없으면 0 반환, 여기에 1 더해 품목 개수 업데이트

        if discount_10day == want_dict:
            # 현재 10일 동안 할인 품목과 개수가 원하는 품목 개수와 일치하는지 확인
            answer += 1

    return answer