# Bài 107: Viết hàm tính S = CanBacN(x)

x,N=map(int,input('Nhập x và N: ').split(','))
print('căn bậc {0} của {1} = {2}'.format(N,x,pow(x,1/N)))