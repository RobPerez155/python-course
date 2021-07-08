day_hours = 24
week_days = 7

week_hours = day_hours * week_days
print(week_hours)

list(range(1, 5)) # 1, 2, 3, 4
list(range(1, 10, 2)) # 1, 3, 5, 7, 9 - Third argument is a step, so the list increments by 2

# dir() - shows us the available actions for an item, in this case an array 
# >>> dir(list)
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# help(str.upper) - will tell us what .upper will do

# Tuple() is like a like a list[], except it uses () and it is immutable and a little faster
# Dictionary is like a javascript object{}, and an item is a {key: value} pair
student_grades = {'Mary': 90, 'Jim': 80, 'Mark': 70, }
student_grades.values() # -> ([90, 80, 70])
student_grades.keys() # -> (['Mary', 'Jim', 'Mark'])

#  Creating a function
def mean(mylist):
  the_mean = sum(mylist) / len(mylist)
  return the_mean

print(mean([1, 4, 5]))

#  Conditionals with and/or
# x = 1
# y = 1

# if x == 1 and y == 1:
#   print("Yes")
#   else:
#     print("No")

#  User input
def weather_condition(temp):
  if temp > 70:
    return "Warm"
  else:
    return "Cold"

# input("Enter temperature:") - this is how to request user input
user_input = float(input("Enter temperature:")) # input returns a string so converting it to a float allows it work with the above conditional

name_input = input('Enter your name: ')
message = "Hello %s!" % name_input # String interpolation
message = f"Hello {name_input}" # Is the most recent version of interpolation

# Sample Program 

def sentence_maker (phrase):  # This gets an input from the user and adds the appropriate punctuation
  interrogatives = ("how", "who", "what", "why")
  capitalized = phrase.capitalize()
  if phrase.startswith(interrogatives):
    return "{}?".format(capitalized) # This is how we concatenate the ?
  else:
    return "{}.".format(capitalized)

results = [] # Note this is outside of while loop so we can append to it

while True: 
  user_input = input("Say something: ")
  if user_input == "/end":
    break
  else:
    results.append(sentence_maker(user_input))

print(" ".join(results))

#  List comprehension
temps = [221, 234, 340, 230, -9999]

new_temps = []
for temp in temps:
  new_temps.append(temp / 10)
print(new_temps)

#  ------- Using list comprehension ---------
#  Lists can be generated dynamically
new_temps = [temp / 10 for temp in temps]
new_temps = [temp / 10 for temp in temps if temp != -9999] # With if statement
new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps] # Syntax changes with if else statement. This says divide the temp by 10, if the temp is not -9999, else make the temp 0, do this for each temp in the temps list.

print(new_temps)

# Define a function that takes as a parameter a list that contains both integers and strings and returns the list containing only the integers. For example, if I called your function with foo([99, 'no data', 95, 94, 'no data']) should return [99, 95, 94]
def foo(lst):
    return [item for item in lst if isinstance(item, int)]

def foo(lst):
    return [item if isinstance(item, int) else 0 for item in lst]
# return the item if it is an instance of an integer, or else return zero, for each item in lst

def foo(lst):
    return sum([float(item) for item in lst])
# return the sum of the following, convert the item into a float for each item in the list
# This turns a list of strings['4.3', '5.2', '2.8'] into a sum of 12.3

# Use *args to create a function w/ unlimited arguments - below will yield the mean
def barf(*args):
    return sum(args) / len(args)

def dorf(*args):
    args = [x.upper() for x in args] # create a list and iterate through the list and capitalize
    return sorted(args) # Sort list

# Define a function that gets a single string character and a filepath as parameters and returns the number of occurences of that character in the file.
def poo(character, filepath = "bear.txt"):
    with open(filepath) as file:
        content = file.read()
        return content.count(character)

# Write the first 90 characters of bear.txt into a new file
with open("bear.txt") as file:
    content = file.read()
    with open("first.txt", "w") as first:
        first.write(content[:90])