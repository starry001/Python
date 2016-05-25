from io import StringIO
from io import BytesIO

f = StringIO()
print(f.write('hello'))
print(f.write(',world'))
print(f.getvalue())

print('----read stringio---')
f = StringIO('hello\nbob\nsss')
print(f.read())
print(f.read())
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

print('--byteio---------')
f = BytesIO()
a = f.write('中文'.encode('utf-8'))
print(a)
print(type(a))
print(f.getvalue())

# 读取bytes
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())

f = StringIO('Hello World');
# f.write('Hello World');
s = f.readline();
print(s)
# f.seek(0)
print(f.readline())
