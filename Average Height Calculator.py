student_height = input("Input a list of student heights separated by a comma.\n")
student_heights = student_height.split(",")

total_height = 0
for height in student_heights:
  total_height = int(total_height) + int(height)
print(f"Total Height of Students is {total_height}") 

number_of_student = 0
for student in student_heights:
  number_of_student = number_of_student + 1
print(f"Number of Students are {number_of_student}")

average_height = round(total_height / number_of_student)
print(f"Average height of Students = {average_height}")
