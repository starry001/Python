from  types import MethodType
from  enum import Enum, unique


class Student(object):
    __slots__ = ('name', 'age', 'set_age')


s = Student()
s.name = 'hh'
print(s.name)


def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age


ss = Student()
ss.set_age = MethodType(set_age, ss)
ss.set_age(25)
print(ss.age)


class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth


class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def hight(self):
        return self._hight

    @hight.setter
    def hight(self, value):
        self._hight = value

    @property
    def resolution(self):
        return self._width * self._hight


s = Student()
s.score = 20
print(s.score)
s.birth = 30
print(s.age)

screen = Screen()
screen.width = 10
screen.hight = 10
print(screen.resolution)


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration();
        return self.a  # 返回下一个值


for n in Fib():
    print(n)
    # enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Mon
print(day1.value)

for name, member in Weekday.__members__.items():
    print(name, '=>', member.value)


# type()
def fn(self, name='world'):  # 先定义函数
    print('Hello, %s.' % name)

Hello2 = type("Hello", (object,), dict(hello2=fn))
h = Hello2()
h.hello2()
print(type(h))
print(type(Hello2))
