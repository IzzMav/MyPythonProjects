sum = "+"
diff = "-"
mul = "x"
div = "/"
choice = True
while choice:
    print("You want to procede?")
    answer = input()
    answer = answer.lower()
    if answer == 'yes':
        print ("choose an operation then: + , - , x , /")
        operation = input()
        print ("write two numbers")
        num1 = int(input())
        num2 = int(input())

        if operation == sum:
            result = num1+num2
            print (result)
        elif operation == diff:
            if num1 > num2:
                result = num1-num2
                print (result)
            else:
                print (0)
        elif operation == mul:
            result = num1*num2
            print (result)
        elif operation == div:
            if num1 != 0 and num2 != 0:
                result = num1/num2
                print (result)
            else:
                print ("A number cannot be devided by zero!")
    elif answer == 'no':
        choice = False
