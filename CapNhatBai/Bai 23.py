# Bài 23: Đếm số lượng “ước số” của số nguyên dương n

n=int(input('Nhập số nguyên dương n: '))
i=1
cnt=0
while pow(i,2)<=n:
    if n%i==0:
        cnt+=1
        j=n/i
        if i!=j:
            cnt+=1
    i+=1

print('S(n) =',cnt)