# Bài 74: Tính S(x, n) = 1 – x + x^3/3! – x^5/5! + … + (-1)^n+1 * x^2n+1/(2n + 1)!

def GiaiThua(n):
    i=2
    rst=1
    while i<=n:
        rst*=i
        i+=1
    return rst

x,n=map(int,input('Nhap 2 so nguyen x, n: ').split())
rst=1
i=0
while i<=n:
    rst+=pow(-1,i+1)*(pow(x,2*i+1)/GiaiThua(2*i+1))
    i+=1

print('S(x,n) =',rst)