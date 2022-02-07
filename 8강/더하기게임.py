import random
com1 = random.randint(1, 100)
com2 = random.randint(1, 100)
print("1 : {}".format(com1))
print("2 : {}".format(com2))
com = com1 + com2
count = 0
while True:
    count = count + 1
    print('{}번째 도전'.format(count))
    user = int(input('두 수의 더하기 값은?'))
    if user < com:
        print("정답보다 작다")
    elif user > com:
        print("정답보다 크다")
    else:
        print("정답입니다")
        break
com = com1 - com2
count = 0
while True:
    count = count + 1
    print('{}번째 도전'.format(count))
    user = int(input('두 수의 빼기 값은?'))
    if user < com:
        print("정답보다 작다")
    elif user > com:
        print("정답보다 크다")
    else:
        print("정답입니다")
        break
