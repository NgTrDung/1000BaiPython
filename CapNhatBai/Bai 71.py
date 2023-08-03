# Bài 71: Tính S(x, n) = -x + x^2/(1 + 2) – x^3/(1 + 2 + 3) + … + (-1)^n * x^n/(1 + 2 +… + n)

def TongMau(n):
    i=1
    sum=0
    while i<=n:
        sum+=i
        i+=1
    return sum

x,n=map(int,input("Nhập 2 số x, n: ").split())
i=1
sum=0
while i<=n:
    sum+=pow(-1,i)*(pow(x,i)/TongMau(i))
    i+=1

print("S(x,n) =",sum)