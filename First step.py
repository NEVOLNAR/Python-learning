def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

rP = 'result plus ='
rM = 'result minus ='

a = int(input())
b = int(input())

print(rP, plus(a, b), 'and', rM, minus(a, b))
