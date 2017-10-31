def inputFunction():
    n = raw_input("Please input a valid positive integer greater than 2: ")
    if (not check_value(n)):
        n = inputFunction()
    return n

def check_value(some_value):
    try:
        y = int(some_value)
    except ValueError:
        return False
    return y > 1 

n = inputFunction()
print("Finding all prime numbers smaller than " + n + "...")
n = int(n)
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
print(prime_list)
