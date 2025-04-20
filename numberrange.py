def near_thousands(n):
    
    return ((abs(1000-n) <= 100) or (abs(2000-n) <= 100))

print(near_thousands(1000))
print(near_thousands(900))
print(near_thousands(2002))
print(near_thousands(1898))

# #here the function near_thousands is defined to check if a number is within 100 of 1000 or 2000.
# # #the abs function is used to get the absolute value of the difference between the number and 1000 or 2000.
# # #if the absolute value is less than or equal to 100 then the function returns True otherwise it returns False.
# # #the function is then called with the numbers 1000, 900, 2002 and 1898 to check if they are within 100 of 1000 or 2000.
# # #the print function is used to print the final result.