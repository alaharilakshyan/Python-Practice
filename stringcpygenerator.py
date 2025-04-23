def larger_string(text, n):
    result = ""
    
    for i in range(n):
        result = result + text
        
        return result
print(larger_string('lucky', 2))
print(larger_string('.html', 3))

# #here the function larger_string is defined to create a new string by repeating the given string 'text' n times.
# # # #the function takes two arguments: 'text' which is the string to be repeated and 'n' which is the number of times to repeat it.
# # # #the function initializes an empty string 'result' and then uses a for loop to concatenate the string 'text' to 'result' n times.
# # # #finally, the function returns the new string 'result'.
