class student:

  def_init_(self,name,roll_number,cgpa)
   self.name=name
   self.rollno=roll_number
   self.cgpa=cgpa


def sort_students(student.list):
#sort the list of students descending order of CGPA
sorted_student=sorted(student.list,key=lambda student:student.cgpa,
                      reverse=True)
return sorted_student

#Example usage:
student=[
 student ("Hari","A123",7.8)
  student ("srikanth"A124",8.9)
  student ("saumya"),"A125",9.1)
  student("Manidhar","A126",9.8)
]
sorted _students=sort_students(student )
#print the sorted list of students for student in shorted_student:
print("Name:{},Rollno:{},CGpA:{}"format (student.name),
  student.roll_number
                 student.(cgpa))

