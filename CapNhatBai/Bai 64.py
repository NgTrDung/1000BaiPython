# Bài 64: Giải pt bậc 1

a,b=map(int,input('Nhập 2 số a, b: ').split())
if a==0:
    print('Pt vô định') if b==0 else print('Pt vô nghiệm')
else:
    print('x =',-b/a)