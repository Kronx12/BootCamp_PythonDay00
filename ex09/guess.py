import random

response = -1
attemps = 0
rdm = random.randint(1, 99)
print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to " +
      "find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!\n")
while response != rdm:
    print("What's your guess between 1 and 99?\n>> ", end='')
    line = input()
    attemps += 1
    if line == "exit":
        print("Goodbye!")
        exit(0)
    try:
        response = int(line)
        if response > 0 and response < 100:
            if response > rdm:
                print("Too high!")
            elif response < rdm:
                print("Too low!")
            else:
                if rdm == 42:
                    print("The answer to the ultimate question of " +
                          "life, the universe and everything is 42.")
                if attemps == 1:
                    print("Congratulations! You got it on your first try!")
                else:
                    print("Congratulations, you've got it!")
                    print("You won in %d attemps!" % attemps)
        else:
            print("Must be greater than 0 and less than 100")
    except ValueError:
        print("That's not a number.")
