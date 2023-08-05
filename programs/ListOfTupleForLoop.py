def ListOfTuple():
    listOfPeople=[
        ('Akash','Tyagi',"BJB"),
        ('Anil', 'Nayak', "MacFab"),
        ('Devina', 'Nayak', "SMU"),
        ('Abu', 'Tyagi', "INV")
    ]

    print(type(listOfPeople)) # class: list
    print(type(listOfPeople[0][1])) # class: str
    print(type(listOfPeople[0])) # class: tuple

    for a,b,c in listOfPeople:
        print("{} - {}".format(a,b))

ListOfTuple()