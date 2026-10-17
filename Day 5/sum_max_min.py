# built-in method to manual method
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

print("Sum using built-in Python Method")
total_score = sum(student_scores)
print(total_score)

print("Sum using manual method")
total_score_manual = 0
for score in student_scores:
    total_score_manual += score
print(total_score_manual)

print("Max and Min using built-in Python Method")
max_score = max(student_scores)
print(max_score)

min_score = min(student_scores)
print(min_score)

print("Max and Min using manual method")
max_score_manual = student_scores[0]
min_score_manual = student_scores[0]
for score in student_scores:
    if max_score_manual < score:
        max_score_manual = score
    if min_score_manual > score:
        min_score_manual = score

print(max_score_manual)
print(min_score_manual)





