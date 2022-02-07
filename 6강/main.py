# prompt = """
# Enter number:"""
# number = 0
# while number != 100:
#     print(prompt)
#     number = int(input())
# while True:
#     print("ctrl+c를 눌려야 while문을 빠져나갈 수 있습니다.")
# number=0
# max = int(input())
# while number < max:
#     number = number + 1
#     print(number)
# while 3<5:
#     print("3은 5보다 작다") 
# print("숫자 두 개를 작은수부터 입력해주세요.")
# min = int(input())
# max = int(input())
# while min <= max:
#     print(min)
#     min=min + 1
# for number in range(1, 13 , 1):
#     print("{}월".format(number))
# for number in range(1, 21, 1):
#     print(number)
# for number in range(1, 10, 1):
#     print(number)
# # print("숫자 두 개를 작은수부터 입력해주세요")
# for number in range(1, 10):
#     string = '{}*{}={}'.format(3, number, 3 * number)
#     print(string)
for 단 in range(2,10):
    print('{}단 시작'.format(단))
    for number in range(1, 10):
        string = '{}*{}={}'.format(단,number, 단 * number)
        print(string)
    print('{}단 종료'.format(단))
시작단 = int(input('구구단 시작 단을 입력하세요(1~9):'))
끝단 = int(input('구구단 끝 단을 입력하세요(1~9):'))
for 단 in range(시작단, 끝단+1):
    for number in range(1, 10):
        string = '{}*{}={}'.format(단, number, 단*number)
