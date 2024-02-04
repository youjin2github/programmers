def solution(sequence, k):
    ans = []
    end = 0
    total = 0
    for i in range(len(sequence)):
        while total<k and end<len(sequence):
            total+=sequence[end]
            end+=1
        if total == k:
            ans.append((i,end-1))
        total-=sequence[i]
    ans.sort(key = lambda x:(x[1]-x[0]))
    return ans[0]