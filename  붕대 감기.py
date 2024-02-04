def solution(bandage, health, attacks):
    t, x, y = bandage  # 붕대 시전 시간, 초당 회복량, 추가 회복량
    h = health  # 현재 체력
    ta = 0  # 연속 공격 시간

    # 가장 늦은 시간
    time = attacks[-1][0]

    # 각 초마다 발생하는 이벤트를 저장한다. (공격당할 시간: 피해량)
    events = {attack[0]: attack[1] for attack in attacks}

    # 1초부터 시작하여 last_attack_time 까지 반복
    for i in range(1, time + 1):
        if i in events:  # 공격을 받는 경우
            h -= events[i]  
            ta = 0  
            if h <= 0:
                return -1 
        else:  # 공격을 받지 않는 경우
            if ta == t:  # 연속 공격 성공 
                h = min(h + y + x, health) 
                ta = 0  # 연속 공격 시간 초기화
            else:
                h = min(h + x, health)  # 체력 회복
                ta += 1  # 연속 공격 시간 증가

    return h