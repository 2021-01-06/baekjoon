n = int(input())
def less_han(x):
    hans = 0
    if x < 100:
        hans = x
    elif x < 1000:
        hans += 99
        for i in range(100, x+1):
            if int(str(i)[2])-int(str(i)[1]) == int(str(i)[1])-int(str(i)[0]):
               hans += 1
    elif x < 10000:
        hans += 144
        for i in range(1000, x+1):
            if int(str(i)[3])-int(str(i)[2]) == int(str(i)[2])-int(str(i)[1]) == int(str(i)[1])-int(str(i)[0]):
                hans +=1
    print(hans)
less_han(n)
