import json

data = json.load(open("data.json")) # Needed to open our json file

def translate(w):
  if w in data: 
    return data[w]
  else:
    return "Please check your spelling"
  
word = input("Enter word ") # This is a global variable

print(translate(word))