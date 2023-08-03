# Bài 78: Liệt kê tất cả các ước số của số nguyên dương n

n=int(input('Nhap so nguyen duong n: '))
i=1
while i*i<=n:
    if n%i==0:
        print(i,"  ",end="")
        j=n/i
        if j!=i:
            print(j,"  ",end="")
    i+=1
