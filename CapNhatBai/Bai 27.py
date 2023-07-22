# Bài 27: Đếm số lượng “ước số chẵn” của số nguyên dương n

n=int(input('Nhập số nguyên dương n: '))
cnt=0
i=1
while i<=n:
    if(n%i==0):
        if(i%2==0):
            cnt+=1
    i+=1

print('Count = ',cnt)