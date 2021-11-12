def gpa(*args):
    gpa = sum(args)/len(args)
    return gpa
def gpa_group_section(n):
    sum = 0
    i = 0
    for gpa in n:
        sum += gpa
        i +=1
    return sum/i

all = []
gpas1_1 = []
gpas1_2 = []
gpas1 = []
gpas2 = []
gpas2_1 = []
gpas2_2 = []

class Student():
    def __init__(self,first_name,name,group,section,mark1,mark2,mark3):
        self.first_name = first_name
        self.name = name
        self.group = group
        self.section = section
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
    def gpa_student(self):
        gpa_student = gpa(self.mark1,self.mark2,self.mark3)
        if self.group == 1 and self.section == 1:
            gpas1_1.append(gpa_student)
            gpas1.append(gpa_student)
            all.append(gpa_student)
        if self.group == 1 and self.section == 2:
            gpas1_2.append(gpa_student)
            gpas2.append(gpa_student)
            all.append(gpa_student)
        if self.group == 2 and self.section == 1:
            gpas2_1.append(gpa_student)
            gpas1.append(gpa_student)
            all.append(gpa_student)
        if self.group == 2 and self.section == 2:
            gpas2_2.append(gpa_student)
            gpas2.append(gpa_student)
            all.append(gpa_student)
        return gpa_student

student1 = Student("Mohamed","Amer",1,1,10,8,15)
student2 = Student("Ali","Simohamed",1,1,5,20,4)
student1.gpa_student()
student2.gpa_student()
try:
    gpa1_1 = gpa_group_section(gpas1_1) # gpa group 1 section 1
    gpa1_2 = gpa_group_section(gpas1_2) # gpa group 2 section 1
    gpa2_1 = gpa_group_section(gpas2_1) # gpa group 1 section 2
    gpa2_2 = gpa_group_section(gpas2_2) # gpa group 2 section 2
    gpasec1 = gpa_group_section(gpas1) # gpa section 1 
    gpasec2 = gpa_group_section(gpas2) # gpa section 2
    gpa_all = gpa_group_section(all) # gpa promo
except ZeroDivisionError:
    print("empty list")



print(student1.gpa_student())
print(student2.gpa_student())
print(gpa1_1)