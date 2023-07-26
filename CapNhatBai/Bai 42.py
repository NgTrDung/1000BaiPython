'''Bài 42: Cho n là số nguyên dương. Hãy tìm giá trị nguyên dương k lớn nhất sao cho S(k) < n. 
Trong đó chuỗi k được định nghĩa như sau: S(k) = 1 + 2 + 3 + … + k'''

n=int(input('Nhập số nguyên dương n: '))
sum=0
i=0
while sum<n:
    i+=1
    sum+=i

print('S(k) =',i-1)
