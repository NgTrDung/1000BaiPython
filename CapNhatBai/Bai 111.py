# Bài 111: Viết chương trình in ra tam giác cân có độ cao h
# a. Tam giác cân đặc nằm giữa màn hình
# b. Tam giác cân rỗng nằm giữa màn hình
# c. Tam giác vuông cân đặc
# d. Tam giác vuông cân rỗng

def print_isosceles_triangle_filled(h):
    for i in range(h):
        print(' ' * (h - i - 1) + '*' * (2 * i + 1))

def print_isosceles_triangle_empty(h):
    print('*' * (2 * h - 1))
    for i in range(h - 2, 0, -1):
        print('*' + ' ' * (2 * i - 1) + '*')
    print('*')

def print_right_angle_isosceles_triangle_filled(h):
    for i in range(h):
        print('*' * (i + 1))

def print_right_angle_isosceles_triangle_empty(h):
    print('*')
    for i in range(h - 2):
        print('*' + ' ' * i + '*')
    print('*' * h)

h = int(input("Nhap do cao tam giac: "))
print('a)')
print_isosceles_triangle_filled(h)
print('b)')
print_isosceles_triangle_empty(h)
print('c)')
print_right_angle_isosceles_triangle_filled(h)
print('d)')
print_right_angle_isosceles_triangle_empty(h)
