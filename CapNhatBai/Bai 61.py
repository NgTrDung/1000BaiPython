# Bài 61: Hãy kiểm tra các chữ số của số nguyên dương n có giảm dần từ trái sang phải hay không

def check_increasing_digits(n):
    prev_digit = -1  # Khởi tạo biến lưu giá trị chữ số trước đó, đặt là 10 để đảm bảo luôn giảm dần

    while n > 0:
        digit = n % 10  # Lấy chữ số cuối cùng của n
        if digit <= prev_digit:
            return False
        prev_digit = digit
        n //= 10

    return True

# Ví dụ sử dụng hàm check_increasing_digits
n = int(input("Nhập số nguyên dương n: "))
result = check_increasing_digits(n)
if result:
    print(f"Các chữ số của {n} giảm dần từ trái sang phải.")
else:
    print(f"Các chữ số của {n} không giảm dần từ trái sang phải.")