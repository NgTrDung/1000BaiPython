# Bài 8: Tính S(n) = ½ + ¾ + 5/6 + … + 2n + 1/ 2n + 2

n=int(input('Nhập số nguyên dương n: '))
sum=0
i=0
while(i<=n):
    sum+=(2*i+1)/(2*i+2)
    i+=1

print('S(n) =',sum)