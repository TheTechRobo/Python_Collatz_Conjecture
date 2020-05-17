#Collatz Conjecture Program
#Created by Lewis Watson

from time import clock
it_count = 0
n = 0

p = input("Would you like to print all numbers? The downside is that it may slow program speed.\nType Y/N: ")
p = p.lower()
if p == "y":
    p = True
else:
    p = False

def Select_Number():
    print()
    sn = int(input("Select the number you wish to calculate? "))
    if (sn == 0):
        print("This number is invalid.")
        print()
        print()
        Select_Number()
    else:
        Calculate(sn)

def Calculate(n):
    global it_count
    it_count = 0

    start = clock()
    while n != 1:
        if (n % 2):
            n = (n*3+1)
            if p:
                print(n) #Prints All Numbers (Slows Program Speed)
            it_count += 1
        else:
            n = (n//2)
            if p:
                print(n) #Prints All Numbers (Slows Program Speed)
            it_count += 1

    end = clock()
    lolz = format(end-start, ".10f")
    print("The number has reached %s with only %s iterations! (Time taken:  %s seconds.)" % (str(n), str(it_count), lolz))
    print()
    Select_Number()

Select_Number()
