# Remove Duplicate from a list

# List
# [1,2,3,4,5,3,4,5,6,88,66456,34,556,34,5667,3,34,5,6,6,8,3,44,44,44,5,55,55,55,6,6,6,77,77,89,89,89]

def removeDuplicateSet():
    myList =[1,2,3,4,5,3,4,5,6,88,66456,34,556,34,5667,3,34,5,6,6,8,3,44,44,44,5,55,55,55,6,6,6,77,77,89,89,89]
    mySet = set()

    for item in myList:
        mySet.add(item)
        # mySet = mySet.add(item)
        ## its not a variable so assigning is mot required
        #add is not returning anything

    print(mySet)
removeDuplicateSet()