import random

def hi_lo():
    x = random.randint(1, 10)
    guess = 0
    while guess < 3:
        n = int(input("\nPlease enter a number: "))
        if n == x:
            guess += 1
            print("Well done! You guessed the correct answer"
              "in: {0}\n\n".format(guess))
            break
        elif n < x:
            guess += 1
            print("Tad low!, Enter a higher value"
              "\nNumber of guesses: {0}".format(guess))
        else:
            guess += 1
            print("Tad High!, Enter a lower value"
              "\nNumber of guesses: {0}".format(guess))
    else:
        print("Oops! You ran out of all 3 tries!\nBetter luck next time\n\n")


def hi_lo_Binary(Y):
    guess = 0
    start = 0
    end = 1000
    for i in range(0, end+1):
        guess += 1
        mid = (start+end)//2
        if mid < Y:
            start = mid + 1
        elif mid > Y:
            end = mid - 1
        else:
            print("Value {0} found at {1} in {2} gueses!\n\n".format(mid, i, guess))
            break




if __name__ == '__main__':
    while True:
        X = int(input("********** Higher or Lower! **********\n\t"
                      "Please select a choice:\n1.Random Hi-Lo\n2.User based Hi-Lo\n3.Exit\n"))
        if X == 1:
            print(" ~ ~ ~ Welcome to Hi-Lo ~ ~ ~\nRules to game:\n\t1. Guess a number btw 1-10"
                  "\n\t2. You have 3 Guesses only!\n")
            hi_lo()

        elif X == 2:
            print(" ~ ~ ~ Welcome to UB-Hi-Lo ~ ~ ~\nRules to game:\n\t1. Guess a number btw 1-1000"
                  "\n\t2. Let Computer Guess Number of tries!\n\t3. If higher than guess = Enter H\n\t4. If Lower than guess ="
                  "Enter L\n\t5. If Correct = Enter C")
            Y = int(input("\nPlease enter value to find: "))
            hi_lo_Binary(Y)

        elif X == 3:
            exit(0)

        else:
            print("Please Enter Valid Value!\n\n")



