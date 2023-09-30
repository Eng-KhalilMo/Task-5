# 1

# Ask the user for input
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# street = input("Enter your street: ")
# city = input("Enter your city: ")
# country = input("Enter your country: ")

# 2

# # Display the user's input in the specified format
# print(f'"Name: {name}"')
# print(f'"Age: {age}"')
# print(f'"Address: {street}, {city}, {country}"')

# 3

# # Calculate the age after reducing by 5 years
# new_age = age - 5
#
# # Display the dynamic output
# output = f"Hello {name} Your age is {new_age} Years Old, Your Address is {street}, {city}, {country}."
#
# print(output)

# 4

# # Print the types of the variables
# print(f"Type of name: {type(name)}")
# print(f"Type of age: {type(age)}")
# print(f"Type of street: {type(street)}")
# print(f"Type of city: {type(city)}")
# print(f"Type of country: {type(country)}")

# 5

# # Display the dynamic output with all symbols
# output = f'"Hello {name}, How Are You? \\ """ Your Age Is "{age}"" + And Your Country Is: {country}"'
# print(output)

# 6

# # Create a multi-line string with the specified output
# output = f'''"Hello '{name}', How Are You? \
# """ Your Age Is "{age}"" + And
#  Your City Is: {city}'''
#
# print(output)

# 7

# # Define the variable
# name_1 = 'ITF Gsg Python'
#
# # Print the desired letters using indexing
# print(f'First Letter Is "{name_1[0]}"')
# print(f'Third Letter Is "{name_1[2]}"')
# print(f'Last Letter Is "{name_1[-1]}"')

# 8

# name_2 = 'ITF Gsg Python'
#
# print(name_2[-3:])
# print(name_2[:3])
# print(name_2[0:7:2])
# print(name_2[:6:-1])

# 9

# name_3 = "$&$&Mohammed$&$&"
#
# # Find the start and end positions of the name within the string
# start = name_3.find("Mohammed")
# end = start + len("Mohammed")
#
# # Extract the name using slicing
# result = name_3[start:end]
#
# print(result)

# 10

# msg = "I %7 Python And Although I %7 GSG with Zakaria"
#
# # Replace all occurrences of "%7" with "Love"
# msg = msg.replace("%7", "Love")
#
# print(msg)

# 11&12

# num1 = "4"
# num2 = "56"
# num3 = "963"
# num4 = "385"
# num5 = "8719"
# num6 = "87190"
#
# # Format and print the numbers with leading zeros
# print(f"{int(num1):05}")
# print(f"{int(num2):05}")
# print(f"{int(num3):05}")
# print(f"{int(num4):05}")
# print(f"{int(num5):05}")
# print(f"{int(num6):05}")

# 13

# # The difference between (title) and (capitalize) methods
# text = "khalil mohammed"
# result = text.title()
# print(result)
#
# text = "khalil mohammed"
# result = text.capitalize()
# print(result)

# 14

# first_name = "Khalil"
#
# print("***********" + first_name)
# print("***********" + first_name + "***********")
# print(first_name + "***********")

# 15

# name_one = "SaMER"
# name_two = "Abed"
#
# # Print with alternating case
# print(name_one[0].lower() + name_one[1:].upper())
# print(name_two[0].lower() + name_two[1:].upper())
#
# # Print with all lowercase and all uppercase
# print(name_one.lower())
# print(name_two.upper())

# 16

# name_one = "SaMER"
# name_two = "abed"
#
# # Check if name_one contains only uppercase letters
# if name_one.isupper():
#     print("name_one contains only uppercase letters.")
# else:
#     print("name_one does not contain only uppercase letters.")
#
# # Check if name_two contains only lowercase letters
# if name_two.islower():
#     print("name_two contains only lowercase letters.")
# else:
#     print("name_two does not contain only lowercase letters.")

# 17

# name_one = "SaMER"
# name_two = "Abed"
#
# # Check if name_one starts with 'S'
# if name_one.startswith('S'):
#     print("name_one starts with 'S'.")
# else:
#     print("name_one does not start with 'S'.")
#
# # Check if name_two ends with 'HD'
# if name_two.endswith('HD'):
#     print("name_two ends with 'HD'.")
# else:
#     print("name_two does not end with 'HD'.")

# 18

# msg = "I Love Python And Although I Love GSG with Zakaria"
#
# love_count = msg.count('Love')
# t_count = msg.count('t')
#
# print(f"Number of <Love> is: {love_count}")
# print(f"Number of <t> is: {t_count}")

# 19

# msg = "I %7 Python And Although I %7 GSG with Zakaria"
#
# msg = msg.replace("%7", "Love", 1)
#
# print(msg)

# 20

# def is_symmetrical_palindrome(input_str):
#     cleaned_str = ''.join(input_str.split()).replace('.', '').replace(',', '').lower()
#
#     is_palindrome = cleaned_str == cleaned_str[::-1]
#
#     length = len(cleaned_str)
#     if length % 2 == 0:
#         is_symmetrical = cleaned_str[:length // 2] == cleaned_str[length // 2:]
#     else:
#         is_symmetrical = cleaned_str[:length // 2] == cleaned_str[length // 2 + 1:]
#
#     return is_symmetrical, is_palindrome
#
#
# test_cases = [
#     "ZakZak",
#     "Zakaria",
#     "A war at Tarawa.",
#     "madam"
# ]
#
# for input_str1 in test_cases:
#     is_sym, is_pal = is_symmetrical_palindrome(input_str1)
#
#     if is_sym:
#         symmetrical_msg = f"{input_str1} is symmetrical, but"
#     else:
#         symmetrical_msg = f"{input_str1} is NOT symmetrical, and"
#
#     if is_pal:
#         palindrome_msg = f"{input_str1} is a palindrome."
#     else:
#         palindrome_msg = f"{input_str1} is NOT a palindrome."
#
#     print(symmetrical_msg, palindrome_msg)
#     print("################################")
