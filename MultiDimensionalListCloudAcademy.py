def multiList():
    a = ["Akash","Devina","Abu"]
    b = ["Anil","Laxmi","Chetan"]
    c = [a,b]

    print(c)
    #[['Akash', 'Devina', 'Abu'], ['Anil', 'Laxmi', 'Chetan']]

    # print Laxmi
    print(c[1][1])

    #How to add in list
    c[1].append("chotu")
    print(c)

    # this will throw index out of range
    print(c[1][4])


multiList()