student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))


total_student_scores = sum(student_scores)
print(f"Total score using sum function: {total_student_scores}\n")

total = 0
for each in student_scores:
    total+=each

print(f"Total score using for Loop: {total}\n")

max_function = max(student_scores)
min_function = min(student_scores)

print(f"Using function\nMax Number: {max_function}\nMin Number: {min_function}\n")

min_var = student_scores[0]
max_var = student_scores[0]
# use for loop to get MAX & MIN
for each in student_scores:
    if each > max_var:
        max_var = each
    if each < min_var:
        min_var = each

print(f"Using for loop\nMax: {max_var}, Min: {min_var}\n")
