import sys

if len(sys.argv) == 1:
    print("Usage: python operations.py <number1> <number2>")
    print("Example:")
    print("\tpython operations.py 10 3")
elif len(sys.argv) > 3:
    print("InputError: too many arguments")
    print("")
    print("Usage: python operations.py <number1> <number2>")
    print("Example:")
    print("\tpython operations.py 10 3")
else:
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        print("%-13s %d" % ("Sum:", a + b))
        print("%-13s %d" % ("Difference:", a - b))
        print("%-13s %d" % ("Product:", a * b))
        if b != 0:
            print("%-13s" % ("Quotient:"), a / b)
            print("%-13s %d" % ("Remainder:", a % b))
        else:
            print("%-13s %s" % ("Quotient:", "ERROR (div by zero)"))
            print("%-13s %s" % ("Remainder:", "ERROR (modulo by zero)"))
    except ValueError:
        print("InputError: only numbers")
        print("")
        print("Usage: python operations.py <number1> <number2>")
        print("Example:")
        print("\tpython operations.py 10 3")
