# Bài 70: Tính S(n) = 1 – 1/(1 + 2) + 1/(1 + 2 + 3) + … + (-1)^n+1 * 1/(1 + 2 + 3+ … + n)

def TongMau(n):
    i=1
    sum=0
    while i<=n:
        sum+=i
        i+=1
    return sum

n=int(input('Nhập số nguyên dương n: '))
sum=0
i=1
while i<=n:
    sum+=1/TongMau(i)
    i+=1

print('S(n) =',sum)