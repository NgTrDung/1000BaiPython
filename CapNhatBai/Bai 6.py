# Bài 6: Tính S(n) = 1/1×2 + 1/2×3 +…+ 1/n x (n + 1)

n=int(input('Nhập số nguyên dương n: '))
sum=0
i=1
while(i<=n):
    sum+=1/(n*(n+1))
    i+=1
    
print('S(n) =',sum)