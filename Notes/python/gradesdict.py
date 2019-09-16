
grade_book = {
    'susan': [89,70,40,55]
    ,'Ed': [100,99,90,91]
    ,'panita': [99,99,91,98]
}

all_grades_sum = 0
all_grades_count = 0

for name , scores in grade_book.items():
    total = sum(scores)
    print(f'Average of {name} is {total/len(scores):.2f}')
    all_grades_sum += total
    all_grades_count += len(scores)

print(f'class average = {all_grades_sum/all_grades_count:.2f}')
