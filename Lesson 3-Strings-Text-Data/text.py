# Lesson 3: String Basics - Simple Name Builder

# Part 1: Creating string variables
first_name = "Alex"
last_name = "Doe"
favorite_number = '11'
lucky_number = 1
gpa = 4.0
print(f"type of favorite number {type(favorite_number)}")
print(f"type of lucky number {type(lucky_number)}")
# Part 2: Combining strings
full_name = first_name + " " + last_name # must be str + str
print(f"Full Name: {full_name}")
print(f"{first_name}'s gpa is {gpa}")
print(f"{first_name}'s gpa is {gpa-1}")

# Part 3: String repetition
print("=" * 50)
cheer = ("Go " + first_name + "!") * 3
print(cheer)
# Part 4: String length
print(len(first_name))
print(f"Length of cheer: {len(cheer)}")

space= "     "
print(len(space))
# Part 5: Indexing and Slicing
school = "Bergen Tech!"
print(school)
print(f"Length of school: {len(school)}")
print(school[0])

# negative indexing
print(school[-1]) #number of last character
print(school[11])
print(school[len(school)-1])
school = "Bergen Tech"
# Part 6: Creative combinations
