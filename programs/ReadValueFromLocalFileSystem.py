
def readTextFile():
    page = open("mary.txt")
    list=[]
    # print(page.read())
    for line in page:
        list.append(line + str(len(line)))

    # list.append(page.readline())

    print(list)

readTextFile()