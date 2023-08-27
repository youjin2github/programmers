import math
def solution(progresses, speeds):
    ans = []
    num = 1
    # 각 프로세스별로 며칠이 걸리는지 반환 
    time = math.ceil((100-progresses[0])/speeds[0])
    for i in range(1, len(progresses)):
        if time >= math.ceil((100-progresses[i])/speeds[i]):
            num += 1
        else:
            ans.append(num)
            num = 1
            time = math.ceil((100-progresses[i])/speeds[i])
    ans.append(num)
    return ans