# Bài 16: Tính S(n) = x + x^2/1 + 2 + x^3/1 + 2 + 3 + … + x^n/1 + 2 + 3 + …. + N

def TongMau(n):
    sum=0
    i=1
    while(i<=n):
        sum+=i
        i+=1
    return sum

x, n = map(int, input("Nhập số nguyên dương x, n: ").split())
sum=0
i=1
while(i<=n):
    sum+=(pow(x,i))/TongMau(i)
    i+=1

print('S(n) =',sum)