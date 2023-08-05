def findTypeOfVariable(val):
    print(type(val))

findTypeOfVariable(1)
findTypeOfVariable("Akash")
findTypeOfVariable(True)
findTypeOfVariable([1,2,3])
findTypeOfVariable({1,2,3})
findTypeOfVariable({"A":1,"B":6})
findTypeOfVariable(('Akash',"Tyagi",4))
findTypeOfVariable("Akash") # will give string
findTypeOfVariable('Akash',) # will give ttuple ?
# Response
# <class 'int'>
# <class 'str'>
# <class 'bool'>
# <class 'list'>
# <class 'set'>
# <class 'dict'>
# <class 'tuple'>
