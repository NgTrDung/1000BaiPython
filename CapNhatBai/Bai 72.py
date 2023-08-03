# Bài 72: Tính S(x, n) = – x + x^2/2! – x^3/3! + … + (-1)^n * x^n/n!

def GiaiThua(n):
    i=2
    rst=1
    while i<=n:
        rst*=i
        i+=1
    return rst

x,n=map(int,input('Nhap 2 so nguyen x, n: ').split())
rst=0
i=1
while i<=n:
    rst+=pow(-1,i)*(pow(x,i)/GiaiThua(i))
    i+=1

print('S(x,n) =',rst)