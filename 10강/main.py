점수들 = [90, 25, 67, 45, 80, 100, 9, 102345, 0, 5, 60, 60]
number = 0
for 점수 in 점수들:
    number = number +1
    if 점수 >= 60:
        print("{}번 학생은 합격입니다.".format(number))
    else:
        print("{}번 학생은 불합격입니다.".format(number))

print(10)
print(20)
print(30)

for 숫자 in [10, 20, 30]:
    print(숫자)

print(10)
print("-------")
print(20)
print("-------")
print(30)
print("-------")

for 숫자 in [10, 20, 30]:
    print(숫자)
    print("-------")

메뉴 = "김밥"
print("오늘의 메뉴: "+ 메뉴)
메뉴 = "라면"
print("오늘의 메뉴: "+ 메뉴)
메뉴 = "튀김"
print("오늘의 메뉴: "+ 메뉴)

리스트 = ["김밥", "라면", "튀김"]
for 메뉴 in 리스트:
    print("오늘의 메뉴: "+ 메뉴)
리스트 = ["김밥", "라면", "튀김"]
for 메뉴 in 리스트:
    print(메뉴[0])
리스트 = [3, -20, -3, 44]
for 변수 in 리스트:
    if 변수 <0:
        print(변수)
튜플 = (3, 100, 23, 44, 103, 28, 99, 65, 63, 3333)
for 변수 in 튜플:
    if 변수 % 3 == 0:
        print(변수)
동물들 = ['강아지', '고양이', '앵무새']
for 동물 in 동물들:
    print(동물)
동물들 = ["강아지", "고양이", "앵무새"]
for 동물 in 동물들:
    print(동물[0])
동물들 = ['강아지', '고양이', '앵무새', '나무좀벌레']
for 동물 in 동물들:
    글자수 = len(동물)
    print("{} {}".format(동물, 글자수))
리스트 = [1, 2, 3]
for number in 리스트:
    print("3 x {} = {}".format(number, 3 * number))
import 수학
print(수학.더하기(3, 4))
print(수학.빼기(4, 2))
from 수학 import 더하기, 빼기
print(더하기(3, 4))
from 수학 import *
print(더하기(3, 4))
import time
print('현재시각:', time.time())
def manyloop(max):
    t1 = time.time()
    for a in range(max):
        pass
    t2 = time.time()
    print(t2-t1, '초 경과')
number = int(input('숫자를 입력하세요: '))
manyloop(number)
import time
current = time.ctime()
print(current)
list_cur = current.split(' ')
print(list_cur)
for t in list_cur:
    print(t)
