import math
'''
    Clock: 360 do
    => kim gio di chuyen 30 do/h => kim gio di chuyen 30/60 = 0.5 do/m
    => kim phut di chuyen 360/60 = 6 do/m
    do lech giua kim gio va kim phut: x(h)y(m)
    = |x*30 + 0.5*y - 6*y|
'''

h = int(input('Nhap so gio: '))
m = int(input('Nhap so phut: '))

print('Goc lech giua kim gio va kim phut: %.1f' % (abs(h*30 + 0.5*m - 6*m)))