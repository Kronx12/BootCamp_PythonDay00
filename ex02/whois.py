import sys

if len(sys.argv) > 2:
    print("Error")

if (len(sys.argv) == 2):
    try:
        num = int(sys.argv[1])
        if num == 0:
            print("I'm Zero.")
        elif num % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        print("Error")
