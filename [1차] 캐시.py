def solution(cacheSize, cities):
    answer = 0
    data = []
    cities = [c.upper() for c in cities]
    if cacheSize == 0:
        return len(cities) * 5
    else:
        for lru in cities:
            if not lru in data:
                if len(data) == 0:
                    data.append(lru)
                if len(data) < cacheSize:
                    data.append(lru)
                    answer += 5
                else:
                    data.pop(0)
                    data.append(lru)
                    answer += 5
            else:
                data.pop(data.index(lru))
                data.append(lru)
                answer += 1
                
        return answer