from decimal import Decimal

t = (0, 4, 132.42222, 10000, 12345.67)
print("day_%02d, ex_%02d : %.2f, %.2e, %.2e" % (t[0], t[1], t[2],
                                                Decimal(t[3]), Decimal(t[4])))
