people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "John", "house": "Greenwood"},
    {"name": "CJ", "house": "Groove Street"},
]

# def f(person):
#     return person['name']

people.sort(key=lambda person: person["name"])
print(people)
