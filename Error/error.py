import logging
import pdb
import unittest

logging.basicConfig(level=logging.INFO)

try:
    print('try...')
    r = 10 / int(3)
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
finally:
    print('finally...')
print('END')


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('1')
    except Exception as e:
        logging.exception(e)


main()
print('END')


#
# # 抛出异常
# class FooError(ValueError):
#     pass

# assert
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n


def main():
    foo('0')


s = '0'
n = int(s)
logging.info('n = %d' % n)
pdb.set_trace()
print(10 / n)


class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

