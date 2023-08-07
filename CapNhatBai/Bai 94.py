# Bài 94: Viết chương trình in ra tất cả các số lẻ nhỏ hơn 100 trừ các số 5, 7, 93

for i in range (1,100,2):
    if i not in [5,7,93]:
        print(i,' ',end="")