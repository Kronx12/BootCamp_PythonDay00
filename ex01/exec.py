import sys


def reverseWordSentence(Sentence):
    words = Sentence.split(" ")
    newWords = [word[::-1] for word in words]
    newSentence = " ".join(newWords)
    return newSentence


res = ""
for i in range(len(sys.argv) - 1, 0, -1):
    word = sys.argv[i].split()
    word.reverse()
    for k in word:
        tmp_word = reverseWordSentence(k)
        for j in tmp_word:
            if j.isalpha():
                if j.isupper():
                    res += j.lower()
                elif j.islower():
                    res += j.upper()
            else:
                res += j
        res += " "
if len(sys.argv) > 1:
    print(res[:-1])
