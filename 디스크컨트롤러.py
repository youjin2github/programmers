import heapq

def solution(jobs):
    # 총 소요 시간
    answer = 0
    # 현 시간 
    now = 0
    # while 문에서 반복을 수행하면서 +1 씩 진행
    i = 0
    # 시작 시간
    start = -1
    # 힙 리슽 
    heap = []
    
    while i < len(jobs):
        # 진행이 가능한 작업을 heap에 저장
        for j in jobs:
            if start < j[0] <= now:
            # 소요 시간을 기준으로 최소 힙으로 저장, 따라서 순서를 반대로 저장
                heapq.heappush(heap, [j[1], j[0]])

        # 처리할 작업이 존재
        if len(heap) > 0:
            cur = heapq.heappop(heap)
            start = now
            # 작업 종료시간 
            now += cur[0]
            # 작업 종료시간 - 작업 시작시간 
            answer += now - cur[1]
            i += 1
        # 처리할 작업 미존재
        else:
            now += 1
    return answer // len(jobs)