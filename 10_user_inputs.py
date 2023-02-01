# while loop

amount = 0
number = 0

while True:

    number += int(input("Number: "))
    amount += 1
    if amount == 10:
            break


print(f"Numbers in total: {amount}")
print(f"Sum of the numbers: {number}")