import math
def main():
    print("Let us finds the solutions to a quadratic\n")
    #获取二次方程中的a,b,c的值。
    a,b,c=eval(input("Do enter the coefficients (a,b,c):"))
    #求取贝塔
    delta=b*b-4*a*c
    #由贝塔的值判断方程根的情况
    if delta <0:
        #贝塔小于0.方程无解
        print("\nThe equation has no real roots!")
    elif delta == 0:
        x = -b / (2 * a)
        print("\nThere is a double root at",x)
    else:
        x=(-b + math.sqrt(delta)) / (2 * a)
        z=(-b - math.sqrt(delta)) / (2 * a)
        print("x1is{},x2is{}".format(x,z))
print(math.sqrt(4))
main()
