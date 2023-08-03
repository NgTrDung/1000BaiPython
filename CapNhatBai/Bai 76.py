# Bài 76: Kiểm tra số nguyên 4 byte có dạng 3^k hay không

n=int(input('Nhap so nguyen duong n: '))
p=1
k=1
while p<n:
    p*=3
    k+=1

if p==n:
    print(n,'is 3^{0}'.format(k-1))
else:
    print(n,'is not 3^k')
