from datetime import datetime, timedelta

# 현재 시간 구하기
now = datetime.now()

# 특정 시간 생성하기
other_time = datetime(2024, 5, 30, 10, 30, 0)

# 시간 간격 구하기
diff = now - other_time

# 특정 시간과 일정 시간 간격 이후의 시간 구하기
future_time = now + timedelta(days=7, hours=3)

print("현재 시간:", now)
print("다른 시간:", other_time)
print("시간 간격:", diff)
print("일주일 후:", future_time)