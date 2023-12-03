import random

GradeList = []
# Dict = {}
TotalGrades = int(input("How many grades would you like to add? :"))
print("1: Manually Enter Grades")
print("2: Randomly Enter Grades")
choice = int(input("What is your choice? :"))

if choice == 1:
    print("Enter", TotalGrades, "grades: ")
    for i in range(0, TotalGrades):
        grade = int(input())
        GradeList.append(grade)
else:
    for i in range(0, TotalGrades):
        grade = random.randint(50, 100)
        GradeList.append(grade)

def calculateGrade(GradeList):
        for grade in GradeList:
            if grade >= 90:
                print(grade,"/","A")
            elif grade < 90 and grade >= 80:
                print(grade,"/","B")
            elif grade < 80 and grade >= 70:
                print(grade,"/","c")
            elif grade < 70 and grade >= 60:
                print(grade,"/","D")
            else:
                print(grade,"/","F")
            
def answer(GradeList):
      passsum = 0
      failsum = 0
      total = 0
      for grade in GradeList:
        total += 1
        if grade > 70:
         passsum += 1
        else:      
         failsum += 1
      passpercent =( passsum / total )* 100 
      print("Passpercent : ", round(passpercent,2),"%")
      failpercent = 100 - passpercent      
      print("Failpercent : ", round(failpercent,2), "%")

GradeList.sort()
GradeList.reverse()
print("Grades with letters:")
calculateGrade(GradeList)

print("=============================================\n")
print("\t\tGrade Report\n\n=============================================")
answer(GradeList) 
