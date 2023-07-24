# Bài 32: Cho số nguyên dương n. Kiểm tra xem n có phải là số chính phương hay không

import math

n=int(input('Nhập số nguyên dương n: '))
temp=int(math.sqrt(n))
if(pow(temp,2)==n):
    print(n,'là số chính phương')
else:
    print(n,'không là số chính phương')