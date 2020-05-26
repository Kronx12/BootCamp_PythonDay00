import sys
import string

res = []
if len(sys.argv) != 3:
    print("ERROR")
else:
    min_len = 0
    try:
        min_len = int(sys.argv[2])
    except ValueError:
        print("ERROR")
        exit(0)
    text = sys.argv[1]
    text = text.translate(str.maketrans('', '', string.punctuation)).split()
    for i in text:
        if not i.isalpha():
            print("ERROR")
            exit(0)
    for i in text:
        if len(i) > min_len:
            res.append(i)
print(res)
