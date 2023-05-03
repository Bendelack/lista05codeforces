a, b, c, d = map(int,input().split())

if (a / b) == (c / d) or (b / a) == (d / c) or (a / b) == (d / c) or (b / a) == (c / d):
    print('S')
elif (a / c) == (b / d) or (a / c) == (d / b) or (c / a) == (b / d) or (c / a) == (d / b):
    print('S')
elif (a / d) == (b / c) or (a / d) == (c / b) or (d / a) == (b / c) or (a / d) == (c / b):
    print('S')
else:
    print('N')