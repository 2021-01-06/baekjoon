# greedy 같네요

table = [300, 60, 10]

# 맞출수 없는 경우 제외

test = int(input())
if test % 10:
    print(-1)
else:
    # 본 코드 작성
    for time_idx in range(len(table)):
        press_num = test // table[time_idx]
        test -= press_num * table[time_idx]
        print(press_num, end=' ')
