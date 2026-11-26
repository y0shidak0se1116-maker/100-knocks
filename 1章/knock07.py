def make_sentence(x,y,z):
    result = str(x) + "時の" + str(y) + "は" + str(z)
    return result

a = make_sentence(12,"気温",22.4)
print(a)