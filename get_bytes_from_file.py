def getBytesFromFile():
    fp = input("Drag n' Drop the file here: ")
    f = open(fp, 'r', encoding="ASCII").read()
    return " ".join('{0:08b}'.format(ord(x)) for x in f)