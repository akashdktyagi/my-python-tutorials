
def readTextFileAndCountMaxCharInLine():
    # Text file contains below:
    # Akash
    # Devina
    # Aavya
    # harimaya
    page = open("mary.txt")

    print(len(x) for x in page) # ==> Generator, nothing in the memory
    # Above will give u: <generator object readTextFileAndCountMaxCharInLine.<locals>.<genexpr> at 0x10bff8cf0>

    print([len(x) for x in page]) # ==> List Comprehensions, memory
    # Above will give u this: [6, 7, 6, 9]
    page.close()

    # need to open it again, because in case of files, once they are iteated
    # the counter reachs the end and then when u try to read it again
    # it returns EOF (end of file) character , so need to open again.
    page = open("mary.txt")
    m = max(len(x) for x in page)
    print(m)
    page.close()

    # list=[]
    # print(page.read())
    # for line in page:
    #     list.append(line + str(len(line)))

    # list.append(page.readline())

    # print(list)

readTextFileAndCountMaxCharInLine()