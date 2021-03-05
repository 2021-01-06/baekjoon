# datetime 쓰는것도 갠찮을텐데 구현해보장
ds = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

# 걍 데이트 타임 쓰자

from datetime import datetime

x, y = map(int, input().split())

time = datetime(2017, 1, 1)
today = datetime.today()
print(time.weekday())

# 낚였네,, 그냥 구현해야하네..
