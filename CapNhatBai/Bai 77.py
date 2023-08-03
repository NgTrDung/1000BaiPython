# Bài 77: Viết chương trình tính tổng của dãy số sau: S(n) = 1 + 2 + 3 + … + n

n=int(input('Nhap so nguyen duong n: '))
sum=1
i=2
while i<=n:
    sum+=n
    i+=1

print('S(n) =',sum)
