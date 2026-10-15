"""
Sum and Difference Calculator
Purpose: Calculates and displays the sum and difference of two numbers provided by the user, using two functions
Author: Luoang
"""

#--Function definitions--
def calculate_sum(): #Calculates and displays the sum of the two numbers
    global num_1, num_2 #Global calls for num_1 and num_2; function now able to use the values of these variables
    num_sum = num_1 + num_2 #local variable; only printed inside this function
    print(f"Sum: {num_sum}")

def calculate_difference(): #Calculates and displays the difference of the two numbers
    global num_1, num_2 #Global calls for num_1 and num_2; function now able to use the values of these variables
    num_diff = num_1 + num_2 #local variable; only printed inside this function
    print(f"Difference: {num_diff}")

#--Main program--
num_1 = float(input("Enter first number: ")) #getting the two numbers from the user as floats
num_2 = float(input("Enter second number: ")) #global variables; can be accessed anywhere
calculate_sum() #calls the two functions
calculate_difference()
    
