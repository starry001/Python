from io import StringIO
from io import BytesIO
import os
import pickle
import json

f = open('../a.txt', 'a')
# print(f.read())
f.write(',aaa')
f.close()

# 用with不需要close
with open('../a.txt', 'r') as f:
    print(f.read())
# open a image
f = open('../python1/test.png', 'rb')
print(f.read())

# StringIO
f = StringIO()
f.write('hello')
f.write(' world')
print(f.getvalue())

s = StringIO('hi\nshsi\nhhh')
while True:
    ss = s.readline()
    if ss == '':
        break
    print(ss.strip())

# BytesIO
f = BytesIO()
f.write('aaa'.encode('utf-8'))
print(f.getvalue())

# OS
print(os.name)
# 查看环境变量
print(os.environ)
print(os.environ.get('PATH'))
# 查看当前目录的绝对路径:
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
os.path.join('.', 'testdir')
# 当前目录下的文件重命名
# os.rename('file.py', 'newfile.py')
# os.remove('test.txt')
d = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print(d)
d2 = [x for x in os.listdir('..') if os.path.isfile(x)]
print(d2)

# 序列化
d = dict(name='Bob', age=20, score=88)
f = open("a.txt", 'wb')
pickle.dump(d, f)
f.close()
f = open("a.txt", 'rb')
d = pickle.load(f)
f.close()
print(d)

# json
d = dict(name='Bob', age=20, score=88)
j = json.dumps(d)
print(j)

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
str = json.loads(json_str)
print(str)


# object to json
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def obj2json(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


s = Student('Bob', 20, 88)
print('---------obj2json----------')
print(json.dumps(s, default=obj2json))

#json to obj
def dict2student(d):
     return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))