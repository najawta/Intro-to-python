# store many items
ages = [21, 72, 43, 76, 23, 88, 78, 90, 15]
names = ["Jane", "Jack", "Rick"]

# functions
ages.append(31)
# ages.clear()
ages.sort()
ages.reverse()
print(ages)

names.sort()
print(names)

jack_count = names.count("Jack")
print(jack_count)

print(len(names))
print(len(ages))

print(sum(ages) / len(ages))

# retrieve an element
print(names[2])

print(names[-1])  # python only start from last
print(names[-2:])  # slicing

# set no duplicates
scores = {88, 44, 67, 88, 21}
print(scores)
scores.add(66)
scores.remove(44)
print(scores)

# tuple imutable
weekdays = ("Mon", "Tue", "Wed", "Thur", "Fri")
print(weekdays[0])

# dictionary
person = {"name": "Jason", "age": 22, "weight": 53, "height": 1.88}
print(person["name"])
print(person["age"])

# dictionary
people = [
    {"name": "Aria", "age": 29},
    {"name": "Moha", "age": 39},
    {"name": "Sam", "age": 80}
]

print(people[2]["age"])
