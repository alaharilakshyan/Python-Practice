def string_adder(text):
    
    if len(text) <= 2 and text[:2] == "Is":
        return text
    else:
        return "Is" + text
    
print(string_adder("Array"))
print(string_adder("IsEmpty"))
#here the function string_adder is defined to add the string "Is" to the beginning of a given string.
# # #if the string is less than or equal to 2 characters and starts with "Is" then the string is returned as it is.
# # #if the string is greater than 2 characters then "Is" is added to the beginning of the string.
# # #the function is then called with the strings "Array" and "IsEmpty" to get the final result.
# # #the print function is used to print the final result.