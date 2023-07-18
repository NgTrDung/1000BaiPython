# Bài 9: Tính T(n) = 1 x 2 x 3…x N

n=int(input('Nhập số nguyên dương n: '))
sum=1
i=1
while(i<=n):
    sum*=i
    i+=1

print('T(n) =',sum)