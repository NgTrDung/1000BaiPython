# Bài 62: Cho 2 số nguyên dương a và b. Hãy tìm ước chung lớn nhất của 2 số này.

def UCLN(a,b):
    while b!=0:
        temp=a%b
        a=b
        b=temp
    return abs(a)

a,b=map(int,input('Nhập 2 số nguyên dương a, b: ').split())
print('UCLN của',a,'và',b,'là',UCLN(a,b))
