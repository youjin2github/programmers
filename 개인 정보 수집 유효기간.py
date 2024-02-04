def solution(today, terms, privacies):
    answer = []
    # 년월일을 분해 - 모두 합 - 일단위로 통일
    y, m, d = today.split('.')
    today = int(y)*12*28 + int(m)*28 + int(d)
    # 약관을 딕셔너리를 이용하여 일단위로 통일
    terms = {i[:1]:int(i[2:])*28 for i in terms}
    # p : privacies를 일 단위로 치환
    # c : 문자의 종류를 나타냄
    for i, p in enumerate(privacies):
        y, m, d = p.split('.')
        d, c = d.split()
        p = int(y)*12*28 + int(m)*28 + int(d)
        if p + terms[c] <= today:
            answer.append(i+1)
    return answer