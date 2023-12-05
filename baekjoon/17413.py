S = input()
tag = False # false 일 경우 뒤집어 출력
word = ''
result = ''

for i in S:
    if tag == False:
        if i == '<':
            tag = True
            word = word + i
        elif i == ' ':
            word = word + i
            result = result + word
            word = '' # 공백 만났을 경우 공백 더해주고 word 초기화
        else:
            # 해당되지 않으면 거꾸로
            word = i + word
    elif tag == True:
        word = word + i
        if i == '>':
            tag = False
            result = result + word
            word = ''

print(result + word)
