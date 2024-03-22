import random


def Fizz_Buzz(n: int) -> str:
    if n%15 == 0:
        return "Fizz - Buzz"
    elif n%3 == 0:
        return "Fizz"
    elif n%5 == 0:
        return "Buzz"
    else:
        return str(n)

def Game():
    print("***** WELCOME TO THE FIZZ-BUZZ *****")
while True:
    val = input('Lets begin! shall we (Y/N): ')
    if val == "N":
        print("Maybe next time!")
        break
    elif val == 'Y':
        count = 3
        while count > 0:
            a = random.randint(1,50)
            ans =  input("\n{0} : Fizz/Buzz/Fizz - Buzz? : ".format(a))
            if ans == Fizz_Buzz(a):
                print("\nWell done! Onto the next one\nTotal Lives: {0}".format(count))
                a = random.randint(1,50)
            else:
                count = count - 1
                print("Oops! try again\nTotal Lives: {0}".format(count))
                a = random.randint(1,50)
        else:
            print("\nSorry :( You lost all lives\nMaybe next time!!")
            break
    else:
        print("Please enter correct value!")
else:
    print("Sorry !")
    exit(0)
