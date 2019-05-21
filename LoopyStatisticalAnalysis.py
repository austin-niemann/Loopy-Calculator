# Austin Niemann 20 May 2019
# this program will calculate stats for numbers between -999 and 999
import math

# introduction to the user
print("Welcome to the Loopy Statistical Analysis program!")
print("This program generates five statistics based on the series of numbers you enter.")
print('''Valid numbers are between -999 and 999. When you are done entering your numbers,
please simply enter a number outside the above specified range.''')

mylist = []
#  user chooses their values to get statistics
user_input = int(input("Enter a new value "))
mylist.append(user_input)

# loop that ends when a number is called outside the limits
while 999 >= user_input >= -999:
    user_input = int(input("Enter a new value "))
    if 999 >= user_input >= -999:
        mylist.append(user_input)

# entries loop ends
print("Exiting Entries... ")

#  beginning of statistics
print("Here are the statistics")
print(mylist)
print("Number of numbers: ", len(mylist))
print("Minimum value: ", min(mylist))
print("Maximum value: ", max(mylist))
average_value = sum(mylist)/ int(len(mylist))
print("The average value is ", average_value)

#  this line is to find the variance
var = sum(pow(x-average_value, 2) for x in mylist) / len(mylist)

#  this line calculates the standard deviation
standard_deviation = math.sqrt(var)

print("The standard deviation is ",standard_deviation)






