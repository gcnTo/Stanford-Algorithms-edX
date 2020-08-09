# To implement it by yourself check out: https://bit.ly/3kn1rqN (edX Course Link)

x = input("Enter the first 4-digit number: ")
y = input("Enter the second 4-digit number: ")

if (len(x) != len(y) or len(x) != 4):
    print("Please enter only 4-digit numbers!")
    x = input("Enter the first 4-digit number: ")
    y = input("Enter the second 4-digit number: ")
    x1 = float(x[0:2])
    x2 = float(x[2:4])
    y1 = float(y[0:2])
    y2 = float(y[2:4])

    step1 = x1 * y1
    step2 = x2 * y2
    step3 = (x1 + x2) * (y1 + y2)
    step4 = step3 - step2 - step1
    step5 = (step1 * 10 ** 4) + step2 + step4 * 100


    print("Number one times number two is: " + str(int(step5)))
    
else:
    x1 = float(x[0:2])
    x2 = float(x[2:4])
    y1 = float(y[0:2])
    y2 = float(y[2:4])

    step1 = x1 * y1
    step2 = x2 * y2
    step3 = (x1 + x2) * (y1 + y2)
    step4 = step3 - step2 - step1
    step5 = (step1 * 10 ** 4) + step2 + step4 * 100
    
    print("Number one times number two is: " + str(int(step5)))
