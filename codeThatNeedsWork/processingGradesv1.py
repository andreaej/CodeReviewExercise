testGrades = ["tests", 100, 85, 78, 0]

hwGrades = ["homework", 93, 45, 88, 100, 76, 96, 99, 82]

projGrades = ["projects", 100, 90, 77]

labGrades = ["labs", 92, 99, 51, 90, 88, 100, 76, 96, 99]


testGrades = [100, 85, 78, 0]
print ("Enter all testGrades with ',' as separator")
testGrades = [int(i) for i in input().split(',')]
print ("Average = ",sum(testGrades)/len(testGrades)) 

hwGrades = ["homework", 93, 45, 88, 100, 76, 96, 99, 82]
print ("Enter all hwGrades with ',' as separator")
hwGrades = [int(i) for i in input().split(',')]
print ("Average = ",sum(hwGrades)/len(hwGrades))

projGrades = ["projects", 100, 90, 77]
print ("Enter all projGrades with ',' as separator")
projGrades = [int(i) for i in input().split(',')]
print ("Average = ",sum(projGrades)/len(projGrades))

labGrades = ["labs", 92, 99, 51, 90, 88, 100, 76, 96, 99]
print ("Enter all labGrades with ',' as separator")
labGrades = [int(i) for i in input().split(',')]
print ("Average = ",sum(labGrades)/len(labGrades)) 
