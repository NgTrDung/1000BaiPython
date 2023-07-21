# Bài 24: Liệt kê tất cả các “ước số lẻ” của số nguyên dương n

def CheckLe(n):
    if(n%2!=0):
        return True
    return False

n=int(input('Nhập số nguyên dương n: '))
i=1
sum=0
while pow(i,2)<=n:
    if n%i==0:
        if(CheckLe(i)==True):
            print(i," ",end="")
        j=n/i
        if i!=j:
            if(CheckLe(j)==True):
                print(j," ",end="")
    i+=1
