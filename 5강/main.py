# pizza = input('피자 가게가 열렸나요(예/아니요)?')
# chicken = input('치킨 가게가 열렸나요(예/아니요)?')
# 편의점 = input('편의점이 열렸나요(예/아니요)?')
# if pizza == '예':
#    print('피자 가게로 가자')
# elif chicken == '예':
#   print('치킨 가게로 가자')
# elif 편의점 == '예':
#    print('편의점으로 가자')
# else:
#    print('집으로 가자')
# if True :
#     print("1")
#     print("2")
# else :
#     print("3")
# print("4")
# print((3 == 3) and (4 != 3))
# if 4 < 3:
#     print("hello world.")
# else:
#     print("hi there")
# data = input("입력값:")
# data = int(data)
# if data +20 > 225:
#     print(225)
# else:
#     print(data + 20)
# data = input("입력값:")
# data = int(data)
# if data -20 < 0:
#     print(0)
# elif data -20 < 225:
#     print(225)
# score = input("점수: ")
# score = int(score)
# if 81 <= score <= 100:
#     print("A등급")
# elif 61 <= score <= 80:
#     print("B등급")
# elif 41 <= score <= 60:
#     print("C등급")
# elif 21 <= score <= 40:
#     print("D등급")
# elif 0 <= score <= 20:
#     print("E등급")
# num1 = input("input number1")
# num2 = input("input number2")
# num3 = input("input number3")
# if num1>num2 and num1>num3:
#     print(num1)
# elif num2>num1 and num2>num3:
#     print(num2)
# elif num3>num1 and num3>num2:
#     print(num3)
# 주민번호 = input("주민등록번호")
# if 주민번호[7]=='1' or 주민번호[7]=='3':
#     print("남자")
# elif 주민번호[7]=='2' or 주민번호[7]=='4':
#     print("여자")
hit = 0
while hit < 10:
    hit =hit +1
    print("나무를 {}번 찍었습니다.".format(hit))
    if hit == 10:
        print("나무가 넘어갔습니다.")
    elif hit == 8:
        print("나무가 곧 넘어갈것 같습니다.")
    elif hit == 3:
        print("나뭇잎이 떨어집니다.")
    elif hit == 1:
        print("나무가 꿈쩍도 하지 않습니다")
    elif hit == 4:
        print("나무가 조금 흔들리고 있습니다")
