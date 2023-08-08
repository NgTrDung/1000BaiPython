# Bài 96: Viết chương trình nhập giá trị x sau tính giá trị của hàm số
# f(x) = 2x^2 + 5x + 9 khi x >= 5, f(x) = -2x^2 + 4x – 9 khi x < 5

def Ptrinh(x):
    return 2*pow(x,2)+5*x+9 if x>=5 else -2*pow(x,2)+4*x-9

x=float(input('Nhập x: '))
print(Ptrinh(x))

