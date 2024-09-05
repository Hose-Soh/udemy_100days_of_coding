student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

def score2grade(score_dict, name):
    if 91<=score_dict[name]<=100:
        return "Outstanding"
    elif 81<=score_dict[name]<=90:
        return "Exceeds Expectations"
    elif 71<=score_dict[name]<=80:
        return "Acceptable"
    elif score_dict[name]<=70:
        return "Fail"
        

student_grades = {}

for key in student_scores:
    student_grades[key] = score2grade(student_scores, key)
    
print(student_grades)