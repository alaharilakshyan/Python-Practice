# def Triple_sum(a, b, c):
    
#     return a + b + c
# if(Triple_sum(2, 4, 6) == 12):
#     print("the sum is equal: ", Triple_sum(2, 4, 6)*3)


def sum_thrice(x,y,z):
    
    sum = x+y+z
    if x==y==z:
        sum = sum*3
        return sum
    
print(sum_thrice(2, 4, 6))
print(sum_thrice(2, 2, 2))
print(sum_thrice(2, 4, 2))
#here the function sum_thrice is defined to calculate the sum of three numbers.
# # #if all three numbers are equal then the sum is multiplied by 3.
# # #the function is then called with the numbers 2, 4, 6, 2, 2, 2 and 2, 4, 2 to get the sum.
# # #the print function is used to print the final result.