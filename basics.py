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