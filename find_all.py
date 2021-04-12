def find_all(txt, pattern, boolean):
    i=0
    x = []
    if boolean == True:
        while i!=-1:

            y = txt.find(pattern, i, len(txt))
            i=y
            if i!=-1:
                x.append(i)
                i+=1

    elif boolean == False:
        while i != -1:

            y = txt.find(pattern, i, len(txt))
            i = y
            if i != -1:
                x.append(i)
                i += len(pattern)


    print(x)


find_all("hello hello hello", "hel", True)
find_all("aaaaaa", "aa", True)
find_all("aaaaaa", "aa", False)
