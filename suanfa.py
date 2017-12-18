t=input("请输入你要累加的数")
if int(t)%2==0:
    a=int(t)*(int(t)/2)+int(t)/2
else:
    a=(int(t)-1)*(int(t)-1)/2+(int(t)-1)/2+int(t)
print(a)
b=0
for i in range(10000001):
    if i==0:
        print(i)
    b+=i
print(b)
