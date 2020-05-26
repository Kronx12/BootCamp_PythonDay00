from time import sleep
from math import *
import os


def ft_progress(listy):
    for i in listy:
        yield int(i * 100 / len(listy))


total = 1000
listy = range(total)
step = 0.001
restant = total * step
time_elapsed = 0
ret = 0
for elem in ft_progress(listy):
    os.system('clear')
    print("ETA: %.2fs [%3d%%]" % (restant,
                                  elem), end='')
    print("[%s>%s] " % ("=" * ceil((elem * 0.01) * 20),
                        " " * floor(((100 - elem) * 0.01) * 20)), end='')
    print("%d/%d elapsed time %.2fs" % (elem * 0.01 * total,
                                        total,
                                        time_elapsed))
    ret += elem
    sleep(step)
    time_elapsed += step
    restant -= step
print("...")
print(ret)
