# scores into grades using dictionary
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key in student_scores:
    value = student_scores[key]
    if value >= 91:
        student_grades[key] = "Outstanding"
    elif value >= 81:
        student_grades[key] = "Exceeds Expectations"
    elif value >= 71:
        student_grades[key] =  "Acceptable" 
    else:
        student_grades[key] = "Fail"

for name in student_grades:
    print(name + " : " + student_grades[name])