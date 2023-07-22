# Bài 26: Tính tích tất cả các “ước số lẻ” của số nguyên dương n

n=int(input('Nhập số nguyên dương n: '))
rst=1
i=1
while i<=n:
    if(n%i==0):
        if(i%2!=0):
            rst*=i
    i+=1
print('S(n) =',rst)