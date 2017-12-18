while True:
    try:
        x=int(input("please enter  number:"))
        break;
    except ValueError:
        print("Oops! That was no valid number. Try again...")
    else:
        print("nihao")
    finally:
        print("wohao")
print(max(1,2,3,4))
