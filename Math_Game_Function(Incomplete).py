import random


def easy():
    X = random.randint(1,20)
    Y = random.randint(1,20)
    count = 1
    Life = 3
    while X != Y  and count <11 and Life != 0:
        Ans1 = X + Y
        Ans = int(input("\nQ{0}. {1} + {2} = ".format(count, X, Y)))
        if Ans1 == Ans:
            print("CORRECT!!! Onto the Next Question!!!!")
            X = random.randint(1,20)
            Y = random.randint(1,20)
        else:
            Life = Life - 1
            print("OOPS! Try next Question!\nTotal Life:", Life)
            X = random.randint(1,20)
            Y = random.randint(1,20)
        count = count + 1

def med():
    X = random.randint(50,100)
    Y = random.randint(50,100)
    count = 1
    Life = 3
    while X != Y  and count <11 and Life != 0:
        Ans1 = X + Y
        Ans = int(input("\nQ{0}. {1} + {2} = ".format(count, X, Y)))
        if Ans1 == Ans:
            print("CORRECT!!! Onto the Next Question!!!!")
            X = random.randint(50,100)
            Y = random.randint(50,100)
        else:
            Life = Life - 1
            print("OOPS! Try next Question!\nTotal Life:", Life)
            X = random.randint(50,100)
            Y = random.randint(50,100)
        count = count + 1

def hard():
    X = random.randint(100,500)
    Y = random.randint(100,500)
    count = 1
    Life = 3
    while X != Y  and count <11 and Life != 0:
        Ans1 = X + Y
        Ans = int(input("\nQ{0}. {1} + {2} = ".format(count, X, Y)))
        if Ans1 == Ans:
            print("CORRECT!!! Onto the Next Question!!!!")
            X = random.randint(100,500)
            Y = random.randint(100,500)
        else:
            Life = Life - 1
            print("OOPS! Try next Question!\nTotal Life:", Life)
            X = random.randint(100,500)
            Y = random.randint(100,500)
        count = count + 1

def nightmare():
    X = random.randint(1000,9999)
    Y = random.randint(1000,9999)
    count = 1
    Life = 3
    while X != Y  and count <11 and Life != 0:
        Ans1 = X + Y
        Ans = int(input("\nQ{0}. {1} + {2} = ".format(count, X, Y)))
        if Ans1 == Ans:
            print("CORRECT!!! Onto the Next Question!!!!")
            X = random.randint(1000,9999)
            Y = random.randint(1000,9999)
        else:
            Life = Life - 1
            print("OOPS! Try next Question!\nTotal Life:", Life)
            X = random.randint(1000,9999)
            Y = random.randint(1000,9999)
        count = count + 1


def difficulty ():
    while True:
        val = input("\nDifficulties\n1.Easy(E)\n2.Medium(M)\n3.Hard(H)\n4.Nightmare!\nChoose a Difficulty(E/M/H/N) : ")
        if val == 'E':
            easy()
        elif val == 'M':
            med()
        elif val == 'H':
            hard()
        elif val == 'N':
            nightmare()
        elif val == '00':
            print("Thank you for playing !!!")
            exit(0)
        else:
            print("\nPlease enter Valid Choice!")


1
if __name__ == '__main__':
    print("*********** WELCOME TO THE MATH GAME **********\nRULES:\n- Answer 10 Questions to win the game\n- You got 3 Lives\n- Operations available: ")
    val = int(input("\t1.ADDITION\n\t2.SUBTRACTION\n\t3.MULTIPLICATION\n\t4.DIVISION\nPlease choose an Operator: "))
    if val == 1:
        difficulty()

