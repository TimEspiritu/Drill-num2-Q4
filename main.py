from pyscript import document

name = "Timothy"
age = 15
height = "5.3 ft"
travel = ["Japan","Italy","France"]
student_type = True
superheros = {"DC": "Batman", "Marvel": "Spider-Man"}
fruits = set(["Mango","Grape","Cherry","Atis","Pear"])

output = f"""
    Name= {name}, Type: {type(name).__name__}
    Age= {age}, Type: {type(age).__name__}
    Height= {height}, Type: {type(height).__name__}
    Countries= {travel}, Type: {type(travel).__name__}
    Student= {student_type}, Type: {type(student_type).__name__}
    Superheros= {superheros}, Type: {type(superheros).__name__}
    fruits= {fruits}, Type: {type(fruits).__name__}

"""

document.querySelector("#output").innerHTML = output
