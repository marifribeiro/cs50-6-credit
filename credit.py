from cs50 import get_string

# ask for input until is digit
while True:
    ccNum = get_string("Number: ")
    if ccNum.isdigit():
        break

# make the string inputed into a list
ccArr = list(ccNum)

# declaration of lists
val0 = []
val1 = []

# if the input is not the right size, screams INVALID
if len(ccArr) < 13 or len(ccArr) > 16:
    print('INVALID')

# if the size of input is valid, let's check if t's a valid card
else:
    # iterates through the credit card numbers, starting from the 2nd to last,
    # skipping 1 until the end of the list
    for i in range(len(ccArr) - 2, -1, -2):
        # declaration of a temp variable that multiplies each number by 2
        tmpInt = int(ccArr[i]) * 2

        # if (number * 2) is 10 or more, lets sum it's products
        if tmpInt > 9:
            tmpStr = str(tmpInt)
            tmpArr = list(tmpStr)
            tmpProd = int(tmpArr[0]) + int(tmpArr[1])
            # and append the sum of the products to the list
            val0.append(tmpProd)
        else:
            # else, just append the number to the list as it is
            val0.append(int(ccArr[i]) * 2)

    # now, append the other numbers to val1 list to add them all
    for i in range(len(ccArr) - 1, -1, -2):
        val1.append(int(ccArr[i]))

    # add both lists to get final verification number
    ver = sum(val1) + sum(val0)

    # before everything, checks if mod of verification number checks
    if ver % 10 == 0:

        # condition to determine if is a mastercard
        if len(ccArr) == 16 and int(ccArr[0]) == 5 and int(ccArr[1]) >= 1 and int(ccArr[1]) <= 5:
            print('MASTERCARD')

        # condition to determine if is a amex
        elif len(ccArr) == 15 and int(ccArr[0]) == 3 and int(ccArr[1]) == 7 or int(ccArr[1]) == 4:
            print('AMEX')

        # condition to determine if is a visa
        elif int(ccArr[0]) == 4:
            print('VISA')

        # if nothing checks, screams INVALID
        else:
            print('INVALID')

    # if verification number don't check, screams INVALID
    else:
        print('INVALID')