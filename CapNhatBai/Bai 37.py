# Bài 37: Tính S(n) = CanBac N(N + CanBac N – 1(N – 1 + … + CanBac3(3 + CanBac2(2))) có n – 1 dấu căn

n=int(input('Nhập số nguyên dương n: '))
sum=0
i=1
while i<=n:
    sum+=pow((i+1)+sum,1.0/(i+1))
    i+=1

print('S(n) =',sum)
