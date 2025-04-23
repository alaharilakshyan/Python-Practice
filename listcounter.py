def list_count(num):
    count = 0
    
    for num in num:
        if num ==4:
            count = count + 1
    return count
print(list_count([1, 4, 5, 4, ]))
print(list_count([1, 4, 6, 7, 4, 4]))
# #here the function list_count is defined to count the number of times the number 4 appears in a given list of numbers.
# # #the function takes a list of numbers as an argument and initializes a variable 'count' to 0.
# # #it then uses a for loop to iterate through each number in the list and checks if the number is equal to 4.
# # #if it is, the count is incremented by 1.
# # #finally, the function returns the total count of 4s in the list.
# # #the function is then called with two different lists to get the final result.