# Bài 75: Kiểm tra số nguyên 4 byte có dạng 2^k hay không

n=int(input('Nhap so nguyen duong n: '))
p=1
k=1
while p<n:
    p*=2
    k+=1

if p==n:
    print(n,'is 2^{0}'.format(k-1))
else:
    print(n,'is not 2^k')