import sys

test_num = int(sys.stdin.readline().strip())

result = []
cnt = 0
stk = []
no_message = True
for _ in range(test_num):
    num = int(sys.stdin.readline().strip())

    while cnt < num:
        result.append("+")
        cnt += 1
        stk.append(cnt)

    if num == stk[-1]:
        stk.pop()
        result.append("-")
    else:
        no_message = False
        break

if no_message == False:
    print("NO")
else:
    print("\n".join(result))