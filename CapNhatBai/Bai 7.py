# Bài 7: Tính S(n) = ½ + 2/3 + ¾ + …. + n / n + 1

n=int(input('Nhập số nguyên dương n: '))
sum=0
i=1
while(i<=n):
    sum+=i/(i+1)
    i+=1

print('S(n) =',sum)