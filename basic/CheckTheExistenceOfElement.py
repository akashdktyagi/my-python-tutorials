def checkTheExistense(s):
    fooList = ["Akash","devina","aavya",1,2,3]
    print(fooList)

    fooSet = {1,2,3,4,5,67,768,45,78,45,67,67,67,889,3,4,5,1,3}
    print(fooSet)

    if s in fooList:
        print(s + " is found in list")
    else:
        print(s + " is not found in list")

    if s in fooSet:
        print( s + "is found in set ")
    else:
        print (s + "is not found in set ")

def takeValueFromUser():
    value = input("enter the value")
    checkTheExistense(value)


takeValueFromUser()