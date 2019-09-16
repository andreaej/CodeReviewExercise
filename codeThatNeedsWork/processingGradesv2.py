#This code will generate a list that iterates 4 lists containing a student's grade
#
#
#Define main function
test= .30
project= .30
lab= .20
hw= .20

def main():
    testGrades= ["tests", 100, 85, 78, 0]
    hwGrades= ["homework", 93, 45, 88, 100, 76, 96, 99, 82]
    projGrades= ["projects", 100, 90, 77]
    labGrades= ["labs", 92, 99, 51, 90, 88, 100, 76, 96, 99]

# Create loop

    for i in range(len(testGrades)):
        if testGrades[i] == "tests":
            total = (sum(testGrades[1: ]) / 4)
    for i in range(len(hwGrades)):
        if hwGrades[i] == "homework":
            total1 = (sum(hwGrades[1: ]) / 8)
    for i in range(len(projGrades)):
        if projGrades[i] == "projects":
            total2= (sum(projGrades[1: ]) / 3)
    for i in range(len(labGrades)):
        if labGrades[i]== "labs":
            total3= (sum(labGrades[1: ]) / 9)

    print("Your final grade is", finalGrade(total, total1, total2, total3))
#Define final grade
   
def finalGrade(total, total1, total2, total3):
     weightedTest = total * test
     weightedHw = total1 * hw
     weightedProject = total2 * project
     weightedLab = total3 * lab
     finalGrade= weightedTest + weightedHw + weightedProject + weightedLab
     result= round(finalGrade, 2)
     return result
#Call main function

main()

    
