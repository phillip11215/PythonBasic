class Animal:
    def eat(self):
        print('먹는다')
    def move(self):
        print('움직인다')
    def sleep(self):
        print('잔다')
class Dog(Animal):
    def bark(self):
        print('멍멍')
    def shake(self):
        print('꼬리를 흔든다')
    def bark2(self):
        print('짖는다')
dog = Dog()
dog.eat()
dog.move()
dog.bark()
dog.shake()
dog.sleep()
dog.bark2()


































class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print('먹는다')
    def move(self):
        print('움직인다')
class Dog(Animal):
    def __init__(self, name, age, owner):
        super().__init__(name, age)
        self.owner = owner
    def bark(self):
        print('멍멍')
    def shake(self):
        print('꼬리를 흔든다')
    def __str__(self):
        sentence = '[이름]:{}, [나이]:{}, [주인]:{}'.format(self.name, self.age, self.owner)
        return sentence
animal = Animal('동물', 1)
animal.eat()
dog = Dog('코코', 2, '홍길동')
dog2 = Dog('몽이', 4, '김평립')
print(dog.name, dog.age, dog.owner)
print(dog)
print(dog2)







































class Animal:
    def eat(self):
        print('먹는다')
    def move(self):
        print('움직인다')
    def sleep(self):
        print('잔다')
class Dog(Animal):
    def bark(self):
        print('멍멍')
    def shake(self):
        print('꼬리를 흔든다')
    def bark2(self):
        print('짖는다')
class Bird(Animal):
    def eat(self):
        print('새가 모이를 먹는다')
    def move(self):
        print('새가 몸을 움직인다')
    def 짹짹(self):
        print('새가 짹짹거린다')
dog = Dog()
bird = Bird()
bird.eat()
bird.move()
bird.짹짹()
dog.bark()
dog.shake()
dog.bark2()

class Human:
    def 때리다(self):
        print('사람을 때리다')
    def 욕쓰다(self):
        print('사람은 욕을 썼다')
class Teacher(Human):
    def 가르치다(self):
        print("선생님은 학생을 가르친다")
    def 수업을끝낸다(self):
        print('선생님은 수업을 끝낸다')
class Student(Human):
    def __init__(self, name, age, grade):
        super().__init__(name, age, grade)
        self.grade = grade
        self.age = age
        self.name = name
    def 공부를한다(self):
        print('학생은 공부를 한다')
    def 학원을다니다(self):
        print('학생은 학원을 다니다')
    def __str__(self):
        sentence = '[이름]:{}, [나이]:{}, [학년]:{}'.format(self.name, self.age, self.grade)
        return sentence
        
teacher = Teacher()
student = Student()
teacher.가르치다()
teacher.수업을끝낸다()
student.공부를한다()
student.학원을다니다()
