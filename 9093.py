# 단어 뒤집기 쉽지
test = int(input())
for i in range(test):
    text_list = input().split()
    for text in text_list:
        print(''.join(list(reversed(text))),end=' ')
    print()