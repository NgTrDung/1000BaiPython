# Bài 73: Tính S(x, n) = -1 + x^2/2! – x^4/4! + … + (-1)^n+1 * x^2n/(2n)!

def GiaiThua(n):
    i=2
    rst=1
    while i<=n:
        rst*=i
        i+=1
    return rst

x,n=map(int,input('Nhap 2 so nguyen x, n: ').split())
rst=0
i=0
while i<=n:
    rst+=pow(-1,i+1)*(pow(x,2*i)/GiaiThua(2*i))
    i+=1

print('S(x,n) =',rst)