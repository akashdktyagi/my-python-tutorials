
def sortThisUsingCustomFnc():
    num1 = ['34',"34","54765","343","45","12","45","0","1","4"]

    # with this I am Passing a function to a function
    # this is an example of lambda expression
    # the sorted() function will take another function, and
    # sorted() function will call this lambda fnc for each of the item automatically
    numSortedList = sorted(num1,key=convert_item_to_int_and_then_sort)

    # IMPORTANT! The above line could been written in pure lambda form
    # numSortedList = sorted(num1,key=lambda x: int(x))

    print(numSortedList)



def convert_item_to_int_and_then_sort(item):
    return int(item)

def sortThis():
    num1 = ['34',"34","54765","343","45","12","45","0","1","4"]
    sortedList = sorted(num1)
    # this was giving wrong output
    print(sortedList) # ['0', '1', '12', '34', '34', '343', '4', '45', '45', '54765']

    # to solve this we need to convert each item to int
    # so we used for loop to convert and then sort
    num1 = ['34',"34","54765","343","45","12","45","0","1","4"]
    num2=[]
    # u can do this or use the below for loop, both works
    # for item in numbers1:
    #     numbers2.append(int(item))

    for i in range(0,len(num1)):
        num2.append(int(num1[i]))

    sortedList1 = sorted(num2)
    # then it gave the right result
    print(sortedList1) # [0, 1, 4, 12, 34, 34, 45, 45, 343, 54765]

sortThis()
sortThisUsingCustomFnc()