#this function can be dramatically shortened by using 
#just one for loop and taking one parameter, it could also return 
#the average which would make the code easier to work with
def average(grade_list):#only asks for one list
  total = 0
  
  #Caluclates average for referenced list
  for elem in grade_list:
    if str(elem).isdigit():#if the element as a string is a digit
      total = total + elem
  testAverage = total/(len(grade_list)-1)
  

 #Weighted Average
  
  weightedAverage(testAverage,hwAverage, projAverage, labAverage)

#i would do something similar to this one
#making it handle one list at a time passing
#the list and the weight as parameters
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
