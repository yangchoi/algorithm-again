def solution(my_string):
    # dictionary: immutable 한 key, immutable 한 value로 매핑되어있는 순서가 없는 집합
    # 키는 immutable한 값 사용가능하나 mutable한 객체는 사용 불가
    # 값은 중복될 수 있으나 키가 중복되면 마지막 값으로 덮어씌워짐
    # 순서가 없어 인덱스로 접근할 수 없고 키로 접근 가능
    # mutable한 객체이므로 키로 접근해 값을 변경할 수 있음
    # fromkeys: key, value 값을 부여한 딕셔너리 값을 만들 수 있다.
    # my_string값을 키로 생성하여 중복되는 것들은 마지막 값으로 덮어씌워진다.
    return ''.join(dict.fromkeys(my_string))
