import re

def solution(files):
    total = []
    # 일단 3부분으로 나눈 값을 리스트에 추가
    for i in range(len(files)):
        total.append(re.split("([0-9]+)", files[i]))
        
    # head부분을 사전 순으로 정렬, 두번째로 number을 정렬하기 
    ## 문자를 대소문자 구분하지 않고 정렬하고 싶다면 .lower()을 붙이기
    total_1 = sorted(total, key = lambda x:[x[0].lower(),int(x[1])])
    
    # 다시 합치기 
    for i in range(len(total_1)):
        total_1[i] = "".join(total_1[i])

    return total_1