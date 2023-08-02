# use curly bracket
# order is not mentained
# duplicates are removed
# true is equal to integer 1
def mySetsFunc():
    fooSet = {2,3,4,5,"Akash",True,2,3,4,5,6}
    print(fooSet)

    # 2nd way fo defining the set
    fooSet1 = set()
    fooSet1.add("1")
    fooSet1.add(1)
    fooSet1.add("Akash")
    fooSet1.add("Akash")
    print(fooSet1)


mySetsFunc()