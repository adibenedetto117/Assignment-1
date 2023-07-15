# Program Title: Fermat’s Last Theorem Near Misses Search
# File Name: assignment1.py
# External Files Needed: None
# External Files Created: None
# Programmers: Anthony DiBenedetto
# Email: anthonypdibenedett@lewisu.edu
# Course Number: CPSC 60500
# Date Finished: <Fill this> | Date Submitted: <Fill this>
# Program Description: This program helps an interactive user search for “near misses" of Fermat's Last Theorem 
#                      by allowing the user to specify n and k.

import math

def head():
    # This function prints the introduction and explanation of the program
    # Also, it waits for the user to press Enter to continue

    print("*"*80)
    print("*"+"Looking for Fermat’s Last Theorem Near Misses".center(78)+"*")
    print("*" +"".center(78) +"*")
    print("*"+"By Anthony DiBenedetto".center(78)+"*")
    print("*"*80,end="\n\n")

    # Displaying the story and explanation to the user

    story = """
    The 17th-century mathematician Pierre Fermat’s sparked 400 years of nightmares for mathematicians 
    by claiming he had a proof for his “last theorem,” but then not providing the proof. Fermat’s last theorem states 
    that there are no natural numbers (1, 2, 3,…) x, y, and z such that x^n + y^n = z^n, in which n is a natural number greater than 2
        """

    print(story,end="\n\n")

    explain = """
    This program helps an interactive user search for “near misses by allowing the user to speficy n and k.”
    N is a natural number greater than 2 and is the exponents used in the equation. K is the upper limit of the x and y
    possibilities.
    """
    print(explain, end="\n\n")

    inp = input("Press Enter to continue...")
    print("")

def errorHandler(error, current_error, x ,y ,z ,n, sum_xy):
    # This function is used to check if the current error is less than the smallest error so far
    # If yes, then it prints the equation and the relative miss and returns the current error
    # If not, it simply returns the smallest error so far
    if current_error < error:
        print(f"{x}^{n:<8} + {y}^{n:<8} = {z}^{n:<8}  {current_error:<15}  {(current_error/sum_xy) * 100}%")
        return current_error
    return error

head()

def main():
    # This function does the main work of the program. 
    # It first gets the values for n and k from the user, checks if they are in the valid range, 
    # and then checks for near misses of Fermat's Last Theorem.

    # Get input from the user for n and k
    step = 0

    while step < 2:
        if step == 0:
            try:
                n = int(input("Enter your value for n ( 2 < n < 12 ): "))
                if 2 < n and n < 12:
                    step+=1
                else :
                    print("Value must be ( 2 < n < 12 )")
            except:
                print("Value for n must be an integer. ")
        elif step  == 1: 
            try:
                k = int(input("Enter your value for k (10 < k): "))
                if 10 < k:
                    step+=1
                else:
                    print("Value for k must be (10 < k)")
            except:
                print("Value must be an integer. ")

    error = math.inf

    print(f"\n{'X':<15}{'Y':<15}{'Z':<15}{'Actual Miss':<15}{'Relative Miss':<15}",end="\n\n")

    # Iterate through x and y and check for near misses
    for x in range(11,k+1):
        for y in range(11,k+1):

            # Calculating the sum of x^n and y^n
            sum_xy = (x**n) + (y**n)
            
            # Special handling when x == y
            if x == y:
                z = math.floor(((sum_xy ** (1/n)) -1))
            else:
                z = math.floor(((sum_xy ** (1/n))))

            z_plusOne = math.floor(((sum_xy ** (1/n)) + 1))
                
            current_error = abs(sum_xy - (z**n))
            error = errorHandler(error,current_error, x, y, z, n, sum_xy)

            current_error = abs(sum_xy - (z_plusOne**n))
            error = errorHandler(error,current_error, x, y, z_plusOne, n, sum_xy)
        
        
again = True

while again:

    main()

    # Allowing the user to quit or try another
    while True:
            q = input("\nEnter 'q' to quit or press enter to try another: ").strip()

            if q == 'q':
                again = False
                break
            elif q == '':
                 print("") 
                 break   
            else:
                print("Invalid..")