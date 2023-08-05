def squareTheNumbers():
    numbers = [1,2,3,4,5,6,7,8,9]

    for i in range(0,len(numbers)):
        numbers[i]=numbers[i]*numbers[i]

    print(numbers)

def squareTheNumbers_theOtherWay():
    numbers = [1,2,3,4,5,6,7,8,9]

    numbers = [x**2 for x in numbers]
    print(numbers)

squareTheNumbers() # [1, 4, 9, 16, 25, 36, 49, 64, 81]
squareTheNumbers_theOtherWay() # [1, 4, 9, 16, 25, 36, 49, 64, 81]