# tech201_control_flow
# Control Flow

# if statements 

`````` python

# Age ratings
U = "Universal - Suitable for all ages"
PG = "Parental Guidance - Suitable for most children"
R12 = "12 - Suitable for ages 12 and over"
R15 = "15 - Suitable for ages 15 and over"
R18 = "18 - Suitable for ages 18 and over"

# User input for age
age = int(input("Please enter your age: "))

# Check if age is valid
if age < 1 or age > 117:
  print("Invalid age entered. Please try again.")


# Check what movies user can watch based on age
elif age < 12:
  print(U)
elif age < 15:
  print(U + PG + R12)
elif age < 18:
  print(U + PG + R12 + R15)
else:
  print(U + PG + R12 + R15 + R18)
``````
The code defines 5 different age ratings: Universal, Parental Guidance, R12, R15, and R18.

The code prompts the user to enter their age and stores it in the "age" variable.

The code checks if the entered age is less than 1 or greater than 117, and if so, it prints an error message.

If the age is within the valid range, the code checks which age ratings the user is eligible to watch based on their age.

If the user's age is less than 12, they can watch Universal rated movies.

If the user's age is between 12 and 14, they can watch Universal and Parental Guidance rated movies.

If the user's age is between 15 and 17, they can watch Universal, Parental Guidance and R12 rated movies.

If the user's age is 18 or above, they can watch movies of all age ratings.

The code then prints the list of eligible age ratings for the user.


# For loops 

A for loop is a control flow structure in programming that repeatedly executes a block of code for a specified number of times or until a specific condition is met.


```` python

list_1 = [1 , 2, 3, 4, 5]

for num in list_1:
    if num == 3:
        print('i found three!')
    elif num == 3:
        print('gone too far')

    else:
        print('too soon')

````


The code defines a list called "list_1" with 5 integers.

The code then uses a for loop to iterate through each integer in the list.

The code checks if the current integer in the loop is equal to 3.

If the integer is equal to 3, the code prints "i found three!".

If the integer is equal to 3 in the second elif clause, it will also print "gone too far".

If the integer is not equal to 3, the code prints "too soon".

The loop repeats for each integer in the list until all integers have been processed.


# While loops:
While loop in Python is a type of loop that repeatedly executes a block of code as long as a certain condition is met. The loop continues until the condition becomes false. The basic syntax of a while loop is as follows: while condition: followed by an indented block of code to be executed repeatedly. The condition is checked at the beginning of each iteration and if it is True, the loop will run again, if the condition is False, the loop will terminate.


`````` python
 while x < 10:
    print(f"its working {x}")
     if x == 4:
         break
    x += 1
 print(x) # X = 4
``````

