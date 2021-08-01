def writeTextToFile(slovo):
    STATICKY_TEXT = "This is my static text which must be added to file. It is very long text and I do not know what they want to do with this terrible text. "
    zretezene = STATICKY_TEXT + str(slovo)
    f = open("zapis.txt", "w")
    f.write(zretezene)
    f.close()
    return "zapis.txt"
