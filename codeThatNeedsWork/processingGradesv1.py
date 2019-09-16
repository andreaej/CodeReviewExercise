testGrades = [100, 85, 78, 0]
hwGrades = [93, 45, 88, 100, 76, 96, 99, 82]
projGrades = [100, 90, 77]
labGrades = [92, 99, 51, 90, 88, 100, 76, 96, 99]


#Defined a function that took the average of of each of the grades
def averageOfGrades(grades):
  print ("Average = ", round(sum(grades)/len(grades),2) )
  
#Called the function for each of the test grades 
averageOfGrades(testGrades)
averageOfGrades(hwGrades)
averageOfGrades(projGrades)
averageOfGrades(labGrades)




































