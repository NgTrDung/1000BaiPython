# Bài 20: Liệt kê tất cả các “ước số” của số nguyên dương n

n=int(input('Nhập số nguyên dương n: '))
i=1
while pow(i,2)<=n:
    if n%i==0:
        print(i,' ',end='')
        j=n/i
        if i!=j:
            print(j,' ',end='')
    i+=1