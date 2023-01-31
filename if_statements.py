# Control Flow

# Control flow --> Flow through a particular decision process.

# if statement create critrea to check variable against

film_rating = "16"
#
# if age >= 18:
#     print("You are the correct age to watch this fild and buy a ticket")

# if age < 18:
#     print("Im afraid you cannot watch this movie you are not old enough")

# elif and else

if film_rating.lower() == "universal":
     print("all age groups can watch this film")

elif film_rating.lower() == "pg":
    print("genral viewing but parental guidence is advise")
elif film_rating.lower() == "12" or film_rating == "12a":
    print("12 rated movies may not be suitable for those under 12")
elif film_rating.lower() == "18":
    print("You must be 18 to watch 1 rated movies in the cinema")

else:
    print("this is not a correct rating, please use universal, pg, 12, 15, 18")


# in python the are no "switch statements" or "case statements"

