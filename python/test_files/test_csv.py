import csv
students = []
with open("student.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "place": row["place"]})

    print(students)
