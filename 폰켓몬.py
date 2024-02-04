def solution(nums):

    # 폰켓몬 종류와 개수를 저장하는 해시 테이블
    hash_table = {} 
    
    # 폰켓몬 종류별 개수를 해시 테이블에 저장
    for num in nums:
        if num in hash_table:
            hash_table[num] += 1
        else:
            hash_table[num] = 1

    max_types = len(nums) // 2  # 선택할 수 있는 폰켓몬 종류의 최댓값
    unique_types = len(hash_table)  # 해시 테이블에 저장된 폰켓몬 종류의 개수
    return min(max_types, unique_types)  # 둘 중 더 작은 값을 반환

