# Bài 25: Tính tổng tất cả các “ước số chẵn” của số nguyên dương n

def CheckChan(n):
    if(n%2==0):
        return True
    return False

n=int(input('Nhập số nguyên dương n: '))
i=1
sum=0
while pow(i,2)<=n:
    if n%i==0:
        if(CheckChan(i)==True):
            sum+=i
        j=n/i
        if i!=j:
            if(CheckChan(j)==True):
                sum+=j
    i+=1

print('S(n) =',sum)