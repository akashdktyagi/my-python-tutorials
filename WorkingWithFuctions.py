def fncAdd(x,y):
    return x+y,x-y

def callFunc():
    add,sub = fncAdd(6,5)
    print(add)
    print(sub)

    myTuple = fncAdd(6,5)
    print(myTuple[0])
    print(myTuple[1])

callFunc()