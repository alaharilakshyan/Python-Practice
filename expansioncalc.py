n = int(input("Enter the number: "))

a1 = int("%s" % n)
a2 = int("%s%s" % (n, n))
a3 = int("%s%s%s" % (n, n, n))

print(a1 + a2 + a3)
# #here the first number is printed as it is and the second number is printed as the first number concatenated with itself and the third number is printed as the first number concatenated with itself twice.
# #used the input function to take the number as input and then print it in the required format.
# #used the int function to convert the string to integer and then used the % operator to concatenate the strings and print it.
# #used the print function to print the final result.