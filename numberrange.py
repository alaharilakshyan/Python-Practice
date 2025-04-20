def Number_range():
    num1 = int(input("enter the num1: "))
    if num1 < 100:
        print("the num is in the range of 100")
        for i in range(1, 100):
            print(i)