# Bài 67: Tính S(x, n) = x – x^2 + x^3 + … + (-1)^n+1 * x^n

x,n=map(int,input('Nhập 2 số x,n: ').split())
i=1
sum=0
while i<=n:
    sum+=pow((-1),i+1)*pow(x,i)
    i+=1

print('S(x,n) =',sum)