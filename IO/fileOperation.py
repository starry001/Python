import os

print(os.name)
print(os.environ)  # 查看环境变量
print(os.environ.get('Path'))  # 具体查看某个环境变量
# 查看当前目录的绝对路径:
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
result = os.path.join(os.path.abspath('.'), 'test')
print(result)
# r = os.makedirs('f:/test')
# os.removedirs('f:/test')
# os.renames('f:/newtest/test', 'f:/test/test1')
# os.mkdir("/tmp")
print(os.path.split('/Users/michael/testdir/file.txt'))
print(os.listdir('.'))  # 列出当前目录下的所有目录
# 列出当前目录下的所有文件夹
print([x for x in os.listdir('.') if os.path.isdir(x)])
# 列出当前目录下的py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])
