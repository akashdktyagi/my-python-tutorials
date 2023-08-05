def listExpression():
    # normal way to make upper case
    list = ["a","b","c","d"]
    uList=[]
    # normal way
    for item in list:
        uList.append(item.upper())
    print(uList) # ['A', 'B', 'C', 'D']

    # But there is a easy way called as list comprehension
    uList = [val.upper() for val in list]
    print(uList)
listExpression()