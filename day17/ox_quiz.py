def solution(quiz):
    answers = []
    for q in quiz:
        question = q.split()
        if question[1] == '-':
            if int(question[0]) - int(question[2]) == int(question[4]):
                answers.append('O')
            else:
                answers.append('X')
        else:
            if int(question[0]) + int(question[2]) == int(question[4]):
                answers.append('O')
            else:
                answers.append('X')
    return answers
