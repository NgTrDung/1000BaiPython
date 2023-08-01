# Bài 63: Cho 2 số nguyên dương a và b. Hãy tìm bội chung nhỏ nhất của 2 số này

def UCLN(a,b):
    while b!=0:
        temp=a%b
        a=b
        b=temp
    return abs(a)

def BCNN(a,b):
    return abs((a*b)/UCLN(a,b))

a,b=map(int,input('Nhập 2 số nguyên dương a, b: ').split())
print('BCNNcủa',a,'và',b,'là',BCNN(a,b))