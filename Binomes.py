import random

# Data
student_list = ["Bilal",
      "Anais",
      "Alexandre",
      "Clément",
      "Elsa",
      "Yasmine",
      "Mathis",
      "Gabrielle",
      "Valérian",
      "Victor",
      "Chloé",
      "Seynabou",
      "Adélie",
      "Emilie",
      "Guillaume",
      "Amaury",
      "Paul"]

if input("Y'a t'il des absents (o/n) : ") == "o":
    nbr = int(input("Combien ? "))
    for i in range(1, nbr+1):
        check = False
        while not check:
            absent = input("Absent {}: ".format(i))
            if absent in student_list:
                student_list.remove(absent)
                check = True
            else:
                print("Erreur: Elève non présent dans la liste")
    
# Créer les binomes
while len(student_list) > 3:
    student1 = student_list.pop(random.randint(0, len(student_list)-1))
    student2 = student_list.pop(random.randint(0, len(student_list)-1))
    print("{} est avec {}".format(student1, student2))
if len(student_list) % 2 == 1:
    print("{}, {} et {} sont ensembles".format(student_list[0], student_list[1], student_list[2]))
else:
    print("{} est avec {}".format(student_list[0], student_list[1]))
