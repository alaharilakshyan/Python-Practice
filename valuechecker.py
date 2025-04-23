def group_member(group_data, n):
    for value in  group_data:
        if n == value:
            return True
        return False
print(group_member(['a', 'b', 'c'], 'a'))  # True
print(group_member(['a', 'b', 'c'], 'd'))  # False
# # #here the function group_member is defined to check if a given value 'n' is present in a list 'group_data'.
# # # #the function takes two arguments: 'group_data' which is the list of values and 'n' which is the value to be checked.
# # # #it then uses a for loop to iterate through each value in the list and checks if the value is equal to 'n'.
# # # #if it is, the function returns True.
# # # #if the loop completes without finding the value, the function returns False.
# # # #the function is then called with two different lists to get the final result.
