def calculate_pc_room_fee(start_time, duration):
    h, m = map(int, start_time.split(':'))
    h = (h + 2) % 24
    fee = 0

    while duration > 0:
        if h <= 4 and duration > 300:
            duration -= (600 - (h * 60 + m))
            h = 10
            m = 0
            fee += 5000
        else:
            h = (h + 1) % 24
            duration -= 60
            fee += 1000
    return fee

# 입력
T = int(input())
result = []
for _ in range(T):
    start_time, duration = input().split()
    duration = int(duration)
    fee = calculate_pc_room_fee(start_time, duration)
    result.append(fee)

# 출력
for fee in result:
    print(fee)
