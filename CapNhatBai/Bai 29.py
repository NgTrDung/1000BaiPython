# Bài 29: Tìm ước số lẻ lớn nhất của số nguyên dương n. Ví dụ n = 100 ước lẻ lớn nhất là 25

n=int(input('Nhập số nguyên dương n: '))
temp=0
i=1
while i<=n:
    if n%i==0:
        if i%2!=0:
            if temp<i:
                temp=i
    i+=1

print('Ước số lẻ lớn nhất là',temp)