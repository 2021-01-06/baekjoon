# ascending or descending?
# or mixed
li = list(map(int, input().split()))

ascending = True
descending = True

for i in range(len(li)-1):
    if li[i+1] > li[i]:
        descending = False
    if li[i+1] < li[i]:
        ascending = False


if ascending:
    print('ascending')
elif descending:
    print('descending')
else:
    print('mixed')