def inputFunction():
    n = input("Please input a valid positive integer greater than 2: ")
    if (not isinstance(n, int) or n < 2):
        n = inputFunction()
    return n

n = inputFunction()
print(n)
