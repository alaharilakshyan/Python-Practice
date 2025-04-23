def substring_copy(text, n):
    
     flen = 2
     
     if flen > len(text):
         flen = len(text)
     substr = text[:flen]
     result = ''
     
     for i in range(n):
         result = result + substr
         return result
print(substring_copy('abcdefg', 3))
print(substring_copy('lakshyan', 2))    
# #here the function substring_copy is defined to create a new string by repeating the first two characters of the given string 'text' n times.
# # # #the function takes two arguments: 'text' which is the string to be repeated and 'n' which is the number of times to repeat it.
# # # #the function initializes a variable 'flen' to 2 and checks if 'flen' is greater than the length of the string 'text'.
# # # #if it is, 'flen' is set to the length of the string 'text'.
# # # #the function then creates a substring 'substr' by taking the first 'flen' characters of the string 'text'.
# # # #it then initializes an empty string 'result' and uses a for loop to concatenate the substring 'substr' to 'result' n times.
# # # #finally, the function returns the new string 'result'.
# # # #the function is then called with two different strings to get the final result.