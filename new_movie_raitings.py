# Movie Rating Program

# Age ratings
# Movie Rating Program

# Age ratings
def movie_rating(age):
  U = "Universal - Suitable for all ages"
  PG = "Parental Guidance - Suitable for most children"
  R12 = "12 - Suitable for ages 12 and over"
  R15 = "15 - Suitable for ages 15 and over"
  R18 = "18 - Suitable for ages 18 and over"

  if age < 1 or age > 117:
    return "Invalid age entered. Please try again."
  elif age < 12:
    return U
  elif age < 15:
    return U + PG + R12
  elif age < 18:
    return U + PG + R12 + R15
  else:
    return U + PG + R12 + R15 + R18


age = int(input("Please enter your age: "))
print(movie_rating(age))
