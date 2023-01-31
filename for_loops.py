# looping

# a for loop is where you define an iterator number and cylce through data (list or dictonary) 'foreac' entry in that data structure

# Creating a for loop

list_data = [1, 2, 3, 4, 5]
embedded_list = [[1, 2, 3] , [4, 5, 6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}

# for num in list_data:
#     print(num * 2)

# nested for loop (used to get individual data in list)

# for data in embedded_list:
#     print(data)
#     for num in data:
#         print(num)

##  looops for dicitionaires

# for item in dict_data.values():
#     for embed_value in item.values():
#         print(embed_value)
#
#
# for items in dict_data.values().
#     print(items['money'])

# Please see Python docs for more you can do with dictionaries and loops.

# Loopps and if statements

list_1 = [1 , 2, 3, 4, 5]

for num in list_1:
    if num == 3:
        print('i found three!')
    elif num == 3:
        print('gone too far')

    else:
        print('too soon')