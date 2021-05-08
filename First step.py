def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def mul(a, b):
    return a * b


rP = 'result plus ='
rM = 'result minus ='
rMu = 'result mutiply = '

a = int(input())
b = int(input())

print(rP, plus(a, b), 'and', rM, minus(a, b), 'and', rMu, mul(a, b))
