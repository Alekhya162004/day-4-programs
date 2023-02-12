def count_student_users(total_users, staff_users):
    if total_users <= 0 or staff_users <= 0 or staff_users > total_users:
        return "Invalid Input"
    non_teaching_staff = staff_users // 3
    staff_users += non_teaching_staff
    student_users = total_users - staff_users
    return student_users
total_users = int(input("Enter the total number of users: "))
staff_users = int(input("Enter the number of staff users: "))
student_users = count_student_users(total_users, staff_users)
if student_users == "Invalid Input":
    print(student_users)
else:
    print("Student Users:",student_users)
