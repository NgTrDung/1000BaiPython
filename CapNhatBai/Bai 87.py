# Bài 87: Tìm số nguyên dương n nhỏ nhất sao cho 1 + 2 + … + n > 10000

sum=0
i=1
while sum<=10000:
    sum+=i
    i+=1

print(i)