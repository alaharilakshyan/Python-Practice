def difference(n):
    
    if n<=17:
        return 17-n
    else:
        return (n-17)*2
    
print(difference(22))
print(difference(10))
#here the function difference is defined to calculate the difference between a number and 17.
# #if the number is less than or equal to 17 then the difference is calculated by subtracting the number from 17.
# #if the number is greater than 17 then the difference is calculated by multiplying the difference between the number and 17 by 2.
# #the function is then called with the numbers 22 and 10 to get the difference.
# #the print function is used to print the final result.