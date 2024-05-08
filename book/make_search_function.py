# 문자열 해시
def polynomial_hash(str):
    p = 31 # 소수
    # 문자열에서 각 문제에 대한 가중치 계산 시 사용
    # 31은 문장려 해싱에서 흔히 사용되는 값
    # 영어 알파벳이 26자이기 때문에 이보다 큰 소수를 선택하는 것이 일반적.
    m = 1_000_000_007 # 버킷 크기
    # 해시 값 범위를 제한하고 모듈로 연산을 통해 해시 값을 작은 범위 내에서 처리
    # 해시 테이블 크기를 제어, 해시 충돌 가능성 관리
    # 매우 큰 소수를 사용해 충돌을 줄이고 해시 함수 분포를 균일하게 하는데 도움을 줌
    hash_value = 0
    for char in str:
        hash_value = (hash_value * p + ord(char)) % m
        # ord() 특정 문자의 유니코드 값 반환
        # (여기서는 영어 소문자이므로 아스키코드값 반환)
        # hash_value * p : 각 문자 위치에 따라 지수적(거듭제곱)으로 가중치 증가시키기
        # + ord(char): 문자의 코드값을 현재까지의 해시값에 더하기
        # % m : 최종 해시값이 정수 m을 넘지 않도록 범위 내로 제한하여 관리 용이하게 만듦
    return hash_value


def solution(string_list, query_list):
    # string_list의 각 문자열에 대해 다항 해시값 계산
    hash_list = [polynomial_hash(str) for str in string_list]

    # query_list의 각 문자열이 string_list에 있는지 확인
    result = []
    for query in query_list:
        query_hash = polynomial_hash(query)
        if query_hash in hash_list:
            result.append(True)
        result.append(False)
    return result