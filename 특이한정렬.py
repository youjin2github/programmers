def solution(numlist, n):
    # n과의 차이를 나타내는 크기만 저장하는 배열을 생성
    chai = []
    for idx, num in enumerate(numlist):
        chai.append([idx,num - n])
    # 절댓값을 기준으로 1차 정렬, 양수를 우선해서 2차 정렬 
    chai = sorted(chai, key = lambda x:(abs(x[1]), -x[1]))
    # 정렬 순서를 나타내는 인덱스
    idx = [i[0] for i in chai]
    # 인덱스에 해당하는 값을 추출해내기 
    answer = []
    for i in idx:
        answer.append(numlist[i])
    return answer