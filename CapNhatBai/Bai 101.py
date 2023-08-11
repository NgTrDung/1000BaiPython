# Bài 101: Viết chương trình nhập tháng, năm. Hãy cho biết tháng đó có bao nhiêu ngày

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def get_days_in_month(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    else:
        return -1

# Nhập tháng và năm từ người dùng
month = int(input("Nhập tháng (1-12): "))
year = int(input("Nhập năm: "))

# Kiểm tra và in số ngày trong tháng
days = get_days_in_month(month, year)
if days == -1:
    print("Tháng không hợp lệ!")
else:
    print(f"Tháng {month} năm {year} có {days} ngày.")
