# Lesson 2 - Numbers: Integers and Floats
# Follow along as we explore all the concepts!

# 1. INTEGERS - Whole Numbers


# TODO: Create some integer variables
favorite_number = 11
lucky_number = 9

# TODO: basic operations
# Addition, subtraction, multiplication, exponent
sum_numbers = favorite_number + lucky_number
difference = favorite_number - lucky_number
product = lucky_number * favorite_number

print(f"Sum Numbers: {sum_numbers}")
print(f"Difference: {difference}")
print(f"Product: {product}")


# TODO: Create a variable and change its value
# Start with lives = 3, then lose one: lives = lives - 1
lives = 3
print(f"Player starts with {lives} lives.")

lives = lives - 1
print(f"After losing one: {lives} lives")
lives += 1 # Shorthand
print(f"After gaining one: {lives} lives")


# TODO: Demonstrate the difference between / and //
# Use 17 and 5 as examples
a=17
b=5
regular_division = a / b
print(f"Regular division: {regular_division}")
remainder = a % b
print(f"Remainder: {remainder}")
print(a / b)
print(a // b)
print(a % b)




# TODO: Show remainder with 17 % 5
# TODO: Check if a number is even or odd
test_number = 23
if test_number % 2 ==0:
    print(f"{test_number} is even")



# TODO: Create some float variables
# TODO: Show float operations
pi = 3.14159
temp = 98.6
price = 19.99
print("Pi: ", pi)
print(f"Pi:{pi}")