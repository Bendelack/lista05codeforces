ca,ba,pa = map(int,input().split())
cr,br,pr = map(int,input().split())

frango = 0
bife = 0
massa = 0

if ca < cr: 
    frango = cr - ca
if ba < br:
    bife = br - ba
if pa < pr:
    massa = pr - pa

soma = bife + frango + massa

print(soma)