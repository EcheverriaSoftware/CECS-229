#Programmer: Miguel Echeverria
#Date: 1/22/2021
#Purpose: Determines if number is positive, negative, or neither.
#Input: An integer
#Output: Postive, negative, or neither
userNum = int(input("Enter a number: "))
if(userNum > 0):
    print("Your number is positive.")
elif(userNum < 0):
    print("Your number is negative.")
else:
    print("Your number is not negative or positive, so it the number must be zero!")
          
