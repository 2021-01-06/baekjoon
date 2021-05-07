# 이모티콘 찾기
happy = 0
sad = 0

text = input().strip()

happy += text.count(':-)')
sad += text.count(':-(')
if happy > sad:
    print('happy')
elif happy < sad:
    print('sad')
elif happy == 0 and sad == 0:
    print('none')
else:
    print('unsure')