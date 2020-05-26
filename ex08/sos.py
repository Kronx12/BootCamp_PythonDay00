import sys

complete = ""
for i in sys.argv[1:]:
    for c in i:
        if not c.isalnum() and c != ' ':
            print("ERROR")
            exit(0)
    complete += i + " "
complete = complete[:-1]
complete = complete.upper()
res = ""
for c in complete:
    if c == ' ':
        res += "/ "
    elif c == 'A':
        res += ".- "
    elif c == 'B':
        res += "-... "
    elif c == 'C':
        res += "-.-. "
    elif c == 'D':
        res += "-.. "
    elif c == 'E':
        res += ". "
    elif c == 'F':
        res += "..-. "
    elif c == 'G':
        res += "--. "
    elif c == 'H':
        res += ".... "
    elif c == 'I':
        res += ".. "
    elif c == 'J':
        res += ".--- "
    elif c == 'K':
        res += "-.- "
    elif c == 'L':
        res += ".-.. "
    elif c == 'M':
        res += "-- "
    elif c == 'N':
        res += "-."
    elif c == 'O':
        res += "--- "
    elif c == 'P':
        res += ".--. "
    elif c == 'Q':
        res += "--.- "
    elif c == 'R':
        res += ".-. "
    elif c == 'S':
        res += "... "
    elif c == 'T':
        res += "- "
    elif c == 'U':
        res += "..- "
    elif c == 'V':
        res += "...- "
    elif c == 'W':
        res += ".-- "
    elif c == 'X':
        res += "-..- "
    elif c == 'Y':
        res += "-.-- "
    elif c == 'Z':
        res += "--.. "
    elif c == '0':
        res += "----- "
    elif c == '1':
        res += ".---- "
    elif c == '2':
        res += "..--- "
    elif c == '3':
        res += "...-- "
    elif c == '4':
        res += "....-"
    elif c == '5':
        res += "....."
    elif c == '6':
        res += "-.... "
    elif c == '7':
        res += "--... "
    elif c == '8':
        res += "---.. "
    elif c == '9':
        res += "----. "
if len(sys.argv) > 1:
    print(res[:-1])
