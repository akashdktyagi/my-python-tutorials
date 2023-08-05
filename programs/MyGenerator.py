def fncGenerator():
    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    s1 = sum([x*x for x in range(10)])

    # it will print the whole list
    print([x*x for x in range(10)])
    print(s1)

    # generator do not store in memory
    s2 = sum(x*x for x in range(10))
    print(s2)
fncGenerator()