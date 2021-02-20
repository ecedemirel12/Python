students = {}

number = input("Student ID: ")
name = input("Student Name: ")
surname = input("Student Surname: ")
phone = input("Phone Number: ")

# students[number] = {
#     'name': name,
#     'surname': surname,
#     'phome': phone
# }  
# OR
students.update({ 
    number: {
        'name': name,
        'surname': surname,
        'phome': phone
    }
})

print(students)

