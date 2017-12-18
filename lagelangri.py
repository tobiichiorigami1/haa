x=eval(input("请输入x："))
y=eval(input("请输入y:"))
d=eval(input("请输入要求的x:"))
n=eval(input("请输入要插的次数"))
L=0
count=0
for i in x:
    count+=1
    if x[count]>d & count+n-1<len(x):
        break;
    else:
        count=len(x)-1-n;
        break;
print(count)
for i in range(count,count+n):
    chengj=1
    chengji=1
    for j in range(count,count+n):
        if(i!=j):
            chengj*=x[i]-x[j]
            chengji*=d-x[j]
            print(x[i]-x[j])
            print(d-x[j])
    L+=y[i]*chengji/chengj
    print(y[i])
print(L)

