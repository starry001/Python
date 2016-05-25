try:
    f = open('test.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

with open('test.txt', 'r') as f:
    print(f.read(3))

with open('msg.png', 'rb') as f:
    print(f.read())

with open('a.txt', 'r', encoding='gbk', errors='ignore') as f:
    print(f.read())

with open('test.txt', 'w') as f:
    f.write('nasikdnkiasd')
    f.close()
