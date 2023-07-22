# Bài 28: Cho số nguyên dương n. Tính tổng các ước số nhỏ hơn chính nó

n=int(input('Nhập số nguyên dương n: '))
sum=0
i=1
while i<n:
    if n%i==0:
        sum+=i
    i+=1

print('S(n) =',sum)