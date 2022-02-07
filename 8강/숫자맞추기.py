import random
print("""- -1을 입력하면 정답을 알수있습니다.
- -100을 입력하면 프로그램을 종료합니다
- 10번내에 맞추세요.
""")
while True:
    print("="*50)
    com = random.randint(0,100)
    #print(com)
    count = 0
    
    while True:
        count = count + 1
        print('{}번째 도전'.format(count))
        print('0~100까지의 숫자를 입력하세요.')
        user = int(input('당신의 선택은?'))
        if count > 9:
            print("실패하였습니다")
            print("정답은{}입니다".format(com))
            break
        if user == -1:
            print("정답은{}입니다".format(com))
            break
        # print(user)
        if user > com:
            print('정답보다 크네요')
        elif user < com:
            print('정답보다 작네요')
        else:
            print('정답입니다')
            break
        if user == -100:
            print("정답은{}입니다".format(com))
            break
    if user == -100:
        break
