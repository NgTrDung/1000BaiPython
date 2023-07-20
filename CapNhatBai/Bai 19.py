# Bài 19: Tính S(n) = 1 + x + x^3/3! + x^5/5! + … + x^(2n+1)/(2n+1)!

def GiaiThua(n):
    rst=1
    i=1
    while(i<=2*n+1):
        rst*=i
        i+=1
    return rst

x,n=map(int,input('Nhập số nguyên dương x, n: ').split())
rst=1
i=1
while(i<=n):
    rst+=(pow(x,2*i+1))/GiaiThua(i)
    i+=1

print('S(n) =',rst)