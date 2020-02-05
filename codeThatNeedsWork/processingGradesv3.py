def average(testGrades,hwGrades,projGrades,labGrades):
  totalTest = 0
  totalHW = 0
  totalProj = 0
  totalLab = 0
  
  #TEST GRADES AVERAGE
  for elem in testGrades:
    if elem != "tests":
      totalTest = totalTest + elem
  testAverage = totalTest/(len(testGrades)-1)
  
  #HOMEWORK GRADES AVERAGE
  for elem in hwGrades:
    if elem != "homework":
      totalHW = totalHW + elem
  hwAverage = totalHW/(len(hwGrades)-1)

  #PROJECT GRADES AVERAGE
  for elem in projGrades:
    if elem != "projects":
      totalProj = totalProj + elem
  projAverage = totalProj/(len(projGrades)-1)

  #LAB GRADES AVERAGE
  for elem in labGrades:
    if elem != "labs":
      totalLab = totalLab + elem
  labAverage = totalLab/(len(labGrades)-1)

 #Weighted Average
  
  weightedAverage(testAverage,hwAverage, projAverage, labAverage)

def weightedAverage(testAverage,hwAverage, projAverage, labAverage):
  weightedTest = testAverage * 0.3
  weightedHW = hwAverage * 0.2
  weightedProj = projAverage * 0.3
  weightedLab = labAverage * 0.2
  
  finalGrade = weightedTest + weightedHW + weightedProj + weightedLab
  print("Your final grade is:", round(finalGrade,2))

def main():
  testGrades = ["tests", 100, 85, 78, 0]
  hwGrades = ["homework", 93, 45, 88, 100, 76, 96, 99, 82]
  projGrades = ["projects", 100, 90, 77]
  labGrades = ["labs", 92, 99, 51, 90, 88, 100, 76, 96, 99]
  average(testGrades,hwGrades,projGrades,labGrades)

main()
