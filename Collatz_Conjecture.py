#Collatz Conjecture Program
#Created by Lewis Watson
#Modified greatly by TheTechRobo

from time import perf_counter_ns
it_count = 0
n = 0

def Select_Number(p=False):
    """
    parameter p: Whether to print or not, default being False.
    """
    global pSelect
    pSelect = p
    if pSelect:
        def p(string):
            print(string, end=", ")
    else:
        def p(string):
            pass
    try:
        sn = int(input("\nEnter the number you wish to calculate: "))
    except Exception as ename:
        raise ValueError("Invalid number.\n\n")
    if (sn == 0):
        raise ValueError("Invalid number.\n\n")
    else:
        Calculate(sn, p)

def Calculate(n, p):
    """
    parameter n: Number to calculate
    parameter p: The function p() that should be passed
    """
    global it_count
    it_count = 0

    start = perf_counter_ns()
    
    while n != 1:
        if (n % 2):
            n = (n*3+1)
            p(n) #If the user enabled printing of the numbers, it prints them. Else it doesnt.
            it_count += 1
        else:
            n = (n//2)
            p(n)
            it_count += 1
    end = perf_counter_ns()
    print ("The number has reached " + str(n) + " with only " + str(it_count) + " iterations! (Time taken: " + format(end-start) + " nanoseconds.)")
    Select_Number(pSelect)

if __name__ == "__main__":
    p = input("Would you like to print all numbers? The downside is that it will drastically slow program speed - for me with a very big number, it was a matter of half a second without, and a minute with.\nType Y/N: ")
    p = p.lower()
    if p[0] == "y":
        Select_Number(p=True)
    else:
        print("Defaulting to DISABLED.")
        Select_Number()
