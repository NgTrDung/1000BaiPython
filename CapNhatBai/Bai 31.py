# Bài 31: Cho số nguyên dương n. Kiểm tra xem n có phải là số nguyên tố hay không

n=int(input('Nhập số nguyên dương n: '))
i=2
flag=1
while pow(i,2)<=n:
    if(n%i==0):
        flag=0
        break
    i+=1

if flag==1:
    print(n,'là số nguyên tố')
else:
    print(n,'không là số nguyên tố')