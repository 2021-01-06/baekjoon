import sys

while True:
    str = sys.stdin.readline().strip("\n")
    if str == '.':
        break
    temp_stk = []
    temp = True
    for word in str:
        if word == '(' or word == '[':
            temp_stk.append(word)
        elif word == ')':
            if not temp_stk or temp_stk[-1] == '[':
                temp = False
                break
            if temp_stk[-1] == '(':
                temp_stk.pop()
        elif word == ']':
            if not temp_stk or temp_stk[-1] == '(':
                temp = False
                break
            if temp_stk[-1] == '[':
                temp_stk.pop()

    if temp and not temp_stk:
         print("yes")
    else:
         print("no")
