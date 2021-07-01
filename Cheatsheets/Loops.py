# For loops are useful for executing a command over a large number of items.

# You can create a for loop like so:

for letter in 'abc':
    print(letter.upper())
# Output:

# A
# B
# C

# The name after for (e.g. letter) is just a variable name



# You can loop over dictionary keys:

phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
for value in phone_numbers.keys():
    print(value)
# Output:

# John Smith
# Marry Simpsons

# You can loop over dictionary values:

phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
for value in phone_numbers.values():
    print(value)
# Output:

+37682929928
+423998200919

# You can loop over dictionary items:

phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
for key, value in phone_numbers.items():
    print(key, value)
# Output: 

('John Smith', '+37682929928')

('Marry Simpons', '+423998200919')



# While loops will run as long as a condition is true:

while datetime.datetime.now() < datetime.datetime(2090, 8, 20, 19, 30, 20):
    print("It's not yet 19:30:20 of 2090.8.20")
# The loop above will print out the string inside print() over and over again until the 20th of August, 2090.

# Note that using loops, you can call any function multiple times, even your own functions. Let's suppose we defined this function:

def celsius_to_kelvin(cels):
    return cels + 273.15
# That is a function that gets a number as input, adds 273.15 to it and returns the result. A for loop allows us to execute that function over a list of numbers:

monday_temperatures = [9.1, 8.8, -270.15]
 
for temperature in monday_temperatures:
    print(celsius_to_kelvin(temperature))
# The output of that would be:

282.25
281.95
3.0

# You can combine a dictionary for loop with string formatting to create text containing information from the dictionary:

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for pair in phone_numbers.items():
    print("{} has as phone number {}".format(pair[0], pair[1]))


# Another (better) way to do it::

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))
# In both cases the output is:

# Output:

# John Smith has as phone number +37682929928

# Marry Simpons has as phone number +423998200919

#  Replace + with 00 and print new phone number
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for value in phone_numbers.values():
    print(value.replace("+", "00"))

# While loop examples
username = ''
while username != "pypy":
  username = input("Enter username: ")

while True:
  username = input("Enter username: ")
  if username == "pypy":
    break
  else:
    continue