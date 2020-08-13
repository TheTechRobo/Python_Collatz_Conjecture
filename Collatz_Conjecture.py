#Collatz Conjecture Program
#Created by Lewis Watson
#Modified greatly by TheTechRobo

from time import clock
it_count = 0
n = 0

def Select_Number(p=False):
    """
    parameter p: Whether to print or not, default being False.
    """
    if p:
        def p(string):
            print(string, end=", ")
    else:
        def p(string):
            pass
    try:
        sn = int(input("\nEnter the number you wish to calculate: "))
    except Exception as ename:
        raise ValueError("Invalid number.\n\n")
        Select_Number()
    if (sn == 0):
        raise ValueError("Invalid number.\n\n")
        Select_Number()
    else:
        Calculate(sn)

def Calculate(n, p):
    """
    parameter n: Number to calculate
    parameter p: The function p() that should be passed
    """
    global it_count
    it_count = 0

    start = clock()
    while n != 1:
        if (n % 2):
            n = (n*3+1)
            p(n) #If the user enabled printing of the numbers, it prints them. Else it doesnt.
            it_count += 1
        else:
            n = (n//2)
            p(n)
            it_count += 1

    end = clock()
    timeTook = format(end-start, ".10f")
    print("The number has reached %s with only %s iterations! (Time taken:  %s seconds.)" % (str(n), str(it_count), timeTook))
    Select_Number()

if __name__ == "__main__":
    p = input("Would you like to print all numbers? The downside is that it may slow program speed.\nType Y/N: ")
    p = p.lower()
    if p[0] == "y":
        Select_Number(p=True)
    else:
        print("Defaulting to DISABLED.")
        Select_Number()
