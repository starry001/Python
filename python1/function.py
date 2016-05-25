import math


def my_add(a, b):
    if not isinstance(a, (int, float)):
        pass
    return a + b


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


def quadratic(a, b, c):
    x = (-b + math.sqrt(b * b - 4 * a * c)) / 2 / a
    y = (-b - math.sqrt(b * b - 4 * a * c)) / 2 / a
    return x, y

def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

def power(x):
    return x * x

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print(abs(1 - 2))
print(str(hex(255)))
print(my_add(1, 2))
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
s = quadratic(1, 2, -3)
print(s)

print(power(5))

list = [1,3,5]
print(calc(*list))

person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)
print(fact(10))