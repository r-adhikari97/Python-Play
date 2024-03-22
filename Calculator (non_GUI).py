def calculator(a, op, b):
    X = 0
    while True:
        if op == '+':
             X = (a+b)
             print(X)
        elif op == '-':
             X = (a-b)
             print(X)
        elif op == '*':
             X = (a*b)
             print(X)
        elif op == '/':
             X = (a/b)
             print(X)
        elif op == 'end':
            print("Exiting calculator.....")
            exit(0)
        else:
            print("Please Enter valid operator")
        a = X
        op = input("\noperator: ")
        b = int(input('Value: '))
        print("\n\n{0} {1} {2}".format(a, op, b))
        calculator(a, op, b)


if __name__ == '__main__':
    print("***** Calculator *****\nPlease enter operands and operators: ")
    x = int(input("\nPlease enter operand 1: "))
    op = input("\nPlease enter Operator: ")
    y = int(input("\nPlease enter operand 2: "))
    print("{0} {1} {2}".format(x,op,y))
    calculator(x, op, y)
