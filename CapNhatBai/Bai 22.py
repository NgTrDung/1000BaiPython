# Bài 22: Tính tích tất cả các “ước số” của số nguyên dương n

n=int(input('Nhập số nguyên dương n: '))
i=1
sum=1
while pow(i,2)<=n:
    if n%i==0:
        sum*=i
        j=n/i
        if i!=j:
            sum*=j
    i+=1

print('S(n) =',sum)