
# ### Exercise 1:
# Print -20 to and including 50. Use any loop you want.
#

for x in range(-20,51,1):
    print(x)


# ### Exercise 2:
# Create a loop that prints even numbers from 0 to and including 20.
# Hint: You can find multiples of 2 with (whatever_number % 2 == 0)
for x in range(0,21,2):
    if x % 2 == 0:
        print(x)


# ### Exercise 3:
# Prompt the user for 3 numbers. Then print the 3 numbers along with their average after the 3rd number is entered.
# Refer to example below replacing ```NUMBER1```, ```NUMBER2```, ```NUMBER3```, and ```THEAVERAGE``` with the actual values.
#
# Ex.Output
# ```
# The average of NUMBER1, NUMBER2, and NUMBER3 is THEAVERAGE

num1 = int(input("Enter a number."))
num2 = int(input("Enter a second number."))
num3 = int(input("Enter a third number."))

average = (num1 + num2 + num3) / 3

print(average)



# ### Exercise 4:
# Use any loop to print all numbers between 0 and 100 that are divisible by 4.
#
#for x in range(0,100,1):
#print (100 % 4 == 0)

for x in range(0,100,1):
    if x % 4 == 0:
        print (x)





# ### Challenge:
# Password Checker - Ask the user to enter a password. Ask them to confirm the password.
# If it's not equal, keep asking until it's correct or they enter 'Q' to quit.

userpassword=input("Enter a password.")
userpassword2=input("Re-enter a password.")

while userpassword != userpassword2:
    print ("Passwords do not match. Please re-enter your password:")
    userpassword2=input()





###