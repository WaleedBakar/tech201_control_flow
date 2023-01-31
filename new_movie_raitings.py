# Movie Rating Program

# Age ratings
# Movie Rating Program

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
