def solution(keymap, targets):
    keytable = {}
    # 그리드 + enumerate + dict 를 활용 -> 영문:인덱스 구조로 만들기
    for keys in keymap:
        for i, key in enumerate(keys):
            if key not in keytable:
                keytable[key] = i+1
            else:
                keytable[key] = min(i+1, keytable[key])
    # targets에 키를 몇번을 눌러야하는지 keytable를 통해 확인
    answer = []
    for target in targets:
        result = 0
        for key in target:
            if key not in keytable:
                result = -1
                break
            else:
                result += keytable[key]
        answer.append(result)
    return answer