class Dog:
    name = "코코"
    age = 2
    def bark(self):
        print('멍멍')
    def move(self):
        print('움직이다')
dog1 = Dog()
dog1.name = '코코'
dog2 = Dog()
dog2.name = '두리'
dog2.age = 4
dog2.weight = 10
print(dog1.name, dog1.age)
print(dog2.name, dog2.age)


































































class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print('{}가 멍멍'.format(self.name))
    def move(self):
        print('{}가 움직인다'.format(self.name))
    def __str__(self):
        sentence = ''
dog1 = Dog('코코', 2)
dog2 = Dog('두리', 4)
dog3 = Dog('몽이', 4)
print(dog1.name, dog1.age)
print(dog2.name, dog2.age)
print(dog3.name, dog3.age)
dog1.bark()
dog2.bark()
dog3.bark()
dog1.move()
dog2.move()
dog3.move()





































class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print('{}가 멍멍'.format(self.name))
    def move(self):
        print('{}가 움직인다'.format(self.name))
    def __str__(self):
        sentence = '[이름]:{}, [나이]:{}'.format(self.name, self.age)
        return sentence
dog1 = Dog('코코', 2)
dog2 = Dog('두리', 4)
dog3 = Dog('몽이', 4)
print(dog1.name, dog1.age)
print(dog2.name, dog2.age)
print(dog3.name, dog3.age)
dog1.bark()
dog2.bark()
dog3.bark()
dog1.move()
dog2.move()
dog3.move()
dog1 = Dog('코코', 2)
dog2 = Dog('두리', 4)
dog3 = Dog('몽이', 4)
print(dog1)
print(dog2)
print(dog3)
















































result = 0
def 더하기(num):
    global result
    result += num
    return result
print(더하기(3))
print(더하기(4))









































class Calculator:
    def __init__(self):
        self.result = 0
    def 더하기(self, num):
        self.result += num
        return self.result
call = Calculator()
print(call.더하기(3))
print(call.더하기(4))











































class Calculator:
    def __init__(self):
        self.result = 0
    def 빼기(self, num):
        self.result -= num
        return self.result
    def 더하기(self, num):
        self.result += num
        return self.result
    def 곱하기(self, num):
        self.result *= num
        return self.result
    def 나누기(self, num):
        self.result /= num
        return self.result
call = Calculator()
print(call.빼기(3))
print(call.빼기(4))
print(call.더하기(9))

call2 = Calculator()
print(call2.빼기(9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999))
print(call2.더하기(22222222222222299999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999))

call3 = Calculator()
print(call3.더하기(1))

call4 = Calculator()
print(call4.더하기(1))
print(call4.빼기(1))
print(call4.곱하기(1))
print(call4.나누기(1))




























































class 학생:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def walk(self):
        print('{}가 걷다'.format(self.name))
    def talk(self):
        print('{}가 발표를 한다'.format(self.name))
    def write(self):
        print('{}가 종이에 쓴다'.format(self.name))
    def __str__(self):
        sentence = '[이름]:{}, [나이]:{}, [학년]:{}'.format(self.name, self.age, self.grade)
        return sentence
학생1 = 학생('김동현', 15, '중2')
학생2 = 학생('김재원', 14, '중1') 
학생3 = 학생('조민준', 13, '초6')
print(학생1)
print(학생2)
print(학생3)
학생1.walk()
학생2.walk()
학생3.walk()
학생1.talk()
학생2.talk()
학생3.talk()
학생1.write()
학생2.write()
학생3.write()
