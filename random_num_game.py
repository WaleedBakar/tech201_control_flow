import random


number = random.randint(1, 20)


for i in range(3):
  guess = int(input("Enter your guess (1-20): "))

  if guess < 1 or guess > 20:
    print("Invalid guess. Please enter a number between 1-20.")
  elif guess < number:
    print("Too low! Guess higher.")
  elif guess > number:
    print("Too high! Guess lower.")
  else:
    print("You got it! The number was", number)
    break
else:
  print("You didn't get it. The number was", number)