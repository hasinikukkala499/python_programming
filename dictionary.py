student={"roll no" :46, "name":"Hasini","branch":"MCA","CGPA":8.1}
print(student)
print(student["name"])
print(student["CGPA"])


student["branch"]="MBA"
student["CGPA"]=8.7
print(student)

student={
"Name":"Rahul",
"CGPA":8.4
}
student["CGPA"]=9.1
print(student)

del student["CGPA"]
print(student)

for key,value in student.items():
    print(key,"=",value)


