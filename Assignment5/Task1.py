dic = {"Alice": 85, "Bob": 90, "Charlie": 78}

name = input("Enter the student's name: ")

# print(f"{name}'s marks: {dic.get(name, 'Student not found.')}")
# print(dic.get(name, 'Student not found.'))
if name in dic:
    print(f"{name}'s marks: {dic[name]}")
else:
    print("Student not found.")