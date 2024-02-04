def solution(babbling):
    answer = 0
    j = ["aya", "ye", "woo", "ma" ]
    for i in babbling:
        for a in j:
            if a*2 not in i:
                i = i.replace(a,' ')
        if i.strip() == '':
            answer += 1
    return answer