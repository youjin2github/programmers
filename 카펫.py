def solution(brown, yellow):
    sum = brown + yellow
    # 두 수를 곱했을때 brown + yellow가 나오는 값을 모두 total에 더하기 
    total = [[sum/n,n] for n in range(1,int((sum)**0.5) + 2) if n > 2 and sum % n == 0]
    # 가로 > 세로, 노란색 크기와 동일한 경우 정답으로 리턴
    for i in total:
        if (i[0]-2)*(i[1]-2) == yellow and i[0] >= i[1]:
            return i
 