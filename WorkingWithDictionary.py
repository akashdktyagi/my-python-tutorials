# dict code
def foo():
    aSet = {}
    aList=[]
    aDict = {"maths":45,"science":56,"civics":67}

    # to retrieve a value from Dict
    print(aDict["maths"]) # 45
    # print(aDict[0]) # this does not work, Dict dnt have indexes

    # 2D dicts
    aTwoDDicts=\
        {
            "Arun": {"m":23,"p":45,"c":67},
            "Devina":{"m":78,"p":34,"c":89},
            "Akash":{"m":25463,"p":566,"c":987}
         }
    print(aTwoDDicts["Devina"]["c"]) # 89

    aTwoDDictsWithList=\
        {
            "Arun": {"m":[45,67],"p":45,"c":67},
            "Devina":{"m":[87,34],"p":34,"c":89},
            "Akash":{"m":[12,75],"p":566,"c":987}
         }
    print(aTwoDDictsWithList["Akash"]["m"][1]) # 75

    # Refresher in List
    list = [1,2,3,4,5,6,7,8,9,0]
    print(list[1:5]) # [2, 3, 4, 5]
    list[1] # 2
    list[2] # 3
    list[1:2] # 2,3

    # 2 D list
    list1=[1,2,3,4,5]
    list2=["a","b","c"]
    list3=['x','y']

    combineList = [list1,list2,list3]
    print(combineList) # [[1, 2, 3, 4, 5], ['a', 'b', 'c']]
    # how to get "c"
    print(combineList[1][2]) # c

foo()