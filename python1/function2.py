import os
from collections import Iterable
from functools import reduce
import  functools
from PIL import Image
import sys

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


def add(x, y, f):
    return f(x) + f(y)


def ff(x):
    return x * x


def fn(x, y):
    return x * 10 + y


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


def is_palindrome(n):
    L = str(n)
    L1 = L[::-1]
    return L == L1


L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2
print(L)

LL = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(LL[0:3])
L = list(range(100))
print(L[::])
print(L[-10:])
print(L[:10])

d = {'a': 1, 'b': 2, 'c': 3}
for key in d.values():
    print("key:", key)

print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance({1: 1, 2: 2, 3: 3}, Iterable))
print(isinstance(123, Iterable))

for k, v in enumerate(['a', 'b', 'c']):
    print(k, v)
for k, v in [(1, 2), (3, 4), (5, 6)]:
    print(k, v)

L = list(range(100))
L1 = L[0:10]
for i, value in enumerate(L1[::2]):
    print(i, value)

l = [x * x for x in range(1, 11) if x % 2 == 0]
print(l)

s = [m + n for m in 'ABC' for n in 'XYZ']
print(s)

dir = [d for d in os.listdir(".")]
print(dir)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)

g = (x * x for x in range(10))
print(g)
for n in g:
    print(n)

f = fib(8)
print(next(f))
print(next(f))
print(next(f))

x = -5
y = 6
f = abs

print(add(x, y, abs))

r = map(ff, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

print(reduce(fn, [1, 2, 3, 4, 5]))
print(char2num('1'))

print(list(filter(is_palindrome, range(10, 1000))))
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0].lower()


def by_score(t):
    return t[1]


LL = sorted(L, key=by_name)
L2 = sorted(L, key=by_score, reverse=True)
print(LL)
print(L2)

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f= lazy_sum(1,3,5,7,9)
print(f())

#偏函数（Partial function）
print(int('11',8))

# int2 = functools.partial(int,base=2)
# print(int2('13'))

im = Image.open('test.png')
print(im.format, im.size, im.mode)
im.thumbnail((200, 100))
im.save("new.png",'PNG')
print(sys.path)