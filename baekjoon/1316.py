num = int(input())
count = 0
for i in range(num):
    word =  input()
    check_word = []
    for idx, w in enumerate(word):
        if w in check_word:
            if check_word[idx - 1] == w:
                check_word.append(w)
            elif check_word[idx - 1] != w:
                check_word.append('*')
        else:
            check_word.append(w)
    if '*' not in check_word:
        count += 1
print(count)