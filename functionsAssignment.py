#QUESTION TWO
# Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# take note of the indentation
#we use the for loop to loop through 
def multiply(mylist):
    product =1
    for x in mylist:
        product *= x
    return product
print(multiply([8,2,3,-1,7]))

#QUESTION TWO
# Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"
def reversed_string(string):
    #slicing the string using string[::-1]
    return string[::-1]
print(reversed_string("1234abcd"))

#QUESTION THREE
# Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]
 
def numbers(even):
    even_numbers = []
    for x in even:
# the x when divided by two gives a remainder of 0(zero)
        if x % 2 == 0:
            even_numbers.append(x)
    return even_numbers
print(numbers([1,2,3,4,5,6,7,8,9]))
