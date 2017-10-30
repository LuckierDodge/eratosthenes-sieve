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

int_list = range(2,int(n)+1)
mark_list = list()

print(n)

for i in range(2,int(n)):
    for j in range(i,int(n)):
        print(j)
