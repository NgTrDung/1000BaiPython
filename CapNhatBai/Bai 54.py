# Bài 54: Hãy đếm số lượng chữ số nhỏ nhất của số nguyên dương n

n = int(input('Nhập số nguyên dương n: '))
temp = n
cnt = 0
min_digit = 10  # Thay min=-1 thành min_digit=10 để đảm bảo khởi tạo min_digit lớn hơn tất cả các chữ số từ 0 đến 9.

while temp != 0:
    numLast = temp % 10
    if min_digit > numLast:
        min_digit = numLast
        cnt = 1
    elif min_digit == numLast:
        cnt += 1
    temp //= 10

print('Chữ số nhỏ nhất trong', n, 'là', min_digit, 'với', cnt, 'lần xuất hiện')
