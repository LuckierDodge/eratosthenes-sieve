### Get a positive integer greater than 2 from the user
def inputFunction():
    n = input("Please input a valid positive integer greater than 2: ")
    if (not checkValue(n)):
        n = inputFunction()
    return int(n)

### Validate input
def checkValue(some_value):
    try:
        y = int(some_value)
    except ValueError:
        return False
    return y > 2 

### Perform Sieve of Erasthosenes Algorithm
def runSieve(n):
    int_list = range(2,n+1)
    mark_list = [False for i in range(2, n+1)]
    prime_list = list(int_list)
    for i in int_list:
        if (mark_list[i-2] == False):
            j = 2
            while i*j <= n:
                if (mark_list[i*j-2] == False):
                    mark_list[i*j-2] = True
                    prime_list.remove(i*j)
                j+=1
    return prime_list

########### Main Wrapper ############
n = inputFunction()
print("Finding all prime numbers smaller than or equal to " + str(n) + "...")
final_list = runSieve(n)
print(final_list)
