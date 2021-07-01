from os import close


#  Longer way to open and close a file
myfile = open("fruits.txt")
content = myfile.read()

print(content)
myfile = close("fruits.txt")

#  Shorter way to open and close a file
with open("fruits.txt") as myfile:
  content = myfile.read()

# once a new non-indented line begins the opened file closes