# students = ["Alice", "Javi", "Damien"]
# students.append("Delilah")
# print(students)
#
# students = ["Alice", "Javi", "Damien"]
# students.insert(1, "Zoe")
# print(students)
#
# students = ["Alice", "Javi", "Damien", "Javi"]
# students.remove("Javi")
# print(students)

# smith_siblings = ["Emily", "Monique", "Giovanni", "Lorenzo", "Julian", "Lil", "Kid"]
# for name in smith_siblings:
#     print(name + " Smith")
#
# smith_siblings = ["Emily", "Monique", "Giovanni", "Brianna", "Javi"]
# for index in range(len(smith_siblings)):
#         smith_siblings[index] = smith_siblings[index] + " Smith"
#
# print(smith_siblings)

# superheroes = ["Captin Marvel", "Wonder Woman", "Storm", "Kamala Khan", "Bumblebee", "Jessica Jones"]
#
# demoted_hero = str(raw_input("What superhero do you want to elminate from the Top 5?"))
# if demoted_hero in superheroes:
#     superheroes.remove(demoted_hero)
#     print("Top 5 heroes:", superheroes)
# else:
#     print("Hero not found.")

names = ["Rickon", "Bran", "Arya", "Sansa", "Jon", "Robb"]

names[::-1]

names[4:2:-1]

print(names[::2])
