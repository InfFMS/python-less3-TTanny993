# с клавиатуры вводится число N, а затем – N натуральных чисел.
# Определить минимальное и максимальное среди простых чисел
# (которые делятся на сами не себя и на 1).
# Если таких чисел не было, вывести "нет".
p=0
x=0
M=-1000
m=1000
y=int(input())
for i in range (1,y+1):
    n=int(input())
    for u in range(2,n):
        if n%u==0:
            x=x+1
    if x==0:
        p=p+1
    if x==0 and n<m:
        m=n
    elif x==0 and n>M:
        M=n
if p==0:
    print("Нет")
else:
    print(M, m)


