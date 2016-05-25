from  types import MethodType


class Student(object):
    def __init__(self, name, score):
        self._name = name;
        self._score = score;

    def print_score(self):
        print('%s: %s' % (self._name, self._score))

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


dog = Dog()
dog.run()

cat = Cat()
cat.run()

print(dir(str))


class Student(object):
    pass


s = Student()
s.name = 'hh'
print(s.name)


def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age


ss = Student()
ss.set_age = MethodType(set_age, ss)
ss.set_age(25)
print(ss.age)
