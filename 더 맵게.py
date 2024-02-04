import heapq
def solution(scoville, K):
    # 섞는 횟수를 answer라는 변수로 설정, 초기값은 0
    answer = 0
    # 주어진 배열을 힙구조로 재배열을 진행, 따라서 가장 작은 값이 가장 먼저 들어오게 된다
    heapq.heapify(scoville) 
    # 만약에 K값 보다 작다면 반복문 진행, K이상으로 설정하는 것이기에 
    while scoville[0] < K:
        # 스코빌의 길이는 2이상임 
        if len(scoville) >= 2:
            # 섞는 횟수를 추가 
            answer += 1
            # 두개를 섞기에 두개는 제거
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            # 새로운 값 추가 
            heapq.heappush(scoville,first + second*2)
        # 만들 수 없으면 -1 리턴
        else:
            return -1
    return answer