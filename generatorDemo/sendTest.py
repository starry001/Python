def gen():
    value = 0
    while True:
        recive = yield value
        if recive == 'e':
            break
        value = 'got: %s' % recive


g = gen()
print(g.send(None))
print(g.send('aaa'))
print(g.send(3))


# print(g.send('e'))

# close test
def g4():
    yield 1
    yield 2
    yield 3


g = g4()
print(next(g))
g.close()
print(next(g))
