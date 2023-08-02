def playingWithList():
    foo = ["Akash", "Devina", "Abu", "Harimaya"]

    # how to append and insert
    foo.append("chotu")
    foo.insert(1, "babu")
    print(foo)
    #['Akash', 'babu', 'Devina', 'Abu', 'Harimaya', 'chotu']

    # How to replace with slicing
    foo[4:5] = ["new maid"] # replace is super easy
    print(foo)
    # ['Akash', 'babu', 'Devina', 'Abu', 'new maid', 'chotu']

    # print with for loop, iterate using for loop
    for bar in foo:
        print(bar)

    # Slicing of list
    print(foo[1:3])
    print(foo[:-1])  # left is inclusive, right id exclusive

    #len of string, its an external function
    print(len(foo))
    # output: 6

    # delete
    del(foo[5])
    print(foo) # this should delete chotu
    #['Akash', 'babu', 'Devina', 'Abu', 'new maid']

    # 2nd way of delete
    foo[4:6]=[]
    print(foo)
    # ['Akash', 'babu', 'Devina', 'Abu']

playingWithList()
