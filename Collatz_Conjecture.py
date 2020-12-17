#Collatz Conjecture Program
#Created by Lewis Watson

from time import perf_counter_ns
it_count = 0
n = 0

def Select_Number():
    print ("")
    sn = int(input("Select the number you wish to calculate? "))
    if (sn == 0):
        print ("This number is invalid.")
        print ()
        print ()
        Select_Number();
    else:
        Calculate(sn);

def Calculate(n):
    global it_count
    it_count = 0

    start = perf_counter_ns()
    
    while n != 1:
        if (n % 2):
            n = (n*3+1)
            #print (n) #Prints All Numbers (Slows Program Speed)
            it_count += 1
        else:
            n = (n//2)
            #print (n) #Prints All Numbers (Slows Program Speed)
            it_count += 1

    end = perf_counter_ns()
    print ("The number has reached " + str(n) + " with only " + str(it_count) + " iterations! (Time taken: " + format(end-start) + " nanoseconds.)")
    print()
    Select_Number();

Select_Number();


