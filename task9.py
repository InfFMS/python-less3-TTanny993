# с клавиатуры вводится число N, а затем – N целых чисел.
# Определить минимальное и максимальное среди двузначных чисел,
# которые делятся на 3. Если таких чисел не было, вывести "нет".
m=1000
M=-1000
n=int(input())
for i in range (1,n+1):
    x=int(input())
    p=str(x)
    if x>M and len(p)==2 and x%3==0:
        M=x
    if x<m and x!=0 and len(p)==2 and x%3==0:
        m=x
if m==1000:
    print('нет')
else:
    print(m)
if M==-1000:
    print('нет')
else:
    print(M)
