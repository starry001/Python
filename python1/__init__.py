
print("hello world")
print(100 + 200)
print('I\'m learning\nPython.')
print(1 == 2)
print(ord('A'))
print(chr(222))
print('\u4e2d\u6587')
print('ABC'.encode('ascii'))

l = ["a", "b", "c"]
print(l)
print(len(l))
print(l[-3])

for str in l:
    print(str)

age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')

    # x = 4;
    # if x:
    #     print("true")
    #
    #     s = input('birth: ')
    # birth = int(s)
    # if birth < 2000:
    #     print('00前')
    # else:
    #     print('00后')

    sum = 0
    for x in range(101):
        sum = x + sum
    print(sum)

list(range(5))

sum = 0
n = 100
while n > 0:
    sum = sum + n
    n = n - 1
print(sum)

L = ['Bart', 'Lisa', 'Adam']

for s in L:
    print("hello,", s)

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d["Bob"])
d["aa"] = "2"
print(d["aa"])
print("aaa" in d)
print(d.get("aaa", -2))

s1 = set([1, 2, 3])
print(s1)
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)

a = ['c', 'b', 'a']
a.sort()
print(a)
st = 'Abcbc'
print(st)
ss= st.replace('A' ,'a')
print(ss)

