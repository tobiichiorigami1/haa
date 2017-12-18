val = input("请输入温度值")
if val[-1] in ['c','C']:
    f=1.8*eval(val[0:-1])+32
    print("转换后的温度为：%.2fF"%f)
elif val[-1] in ['f','F']:
    c=(float(val[0:-1])-32)/18
    print("转换后的温度为：%.2fFC"%c)
else:
    print("输入错误")
    
