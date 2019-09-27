# Program for grading students main script
#
# Author: Nicolai Wolter Hjort Nisbeth, s175565@student.dtu.dk, 2018

#-----------------------------------------------------------------------------
# Import
#-----------------------------------------------------------------------------
import numpy as np
import pandas as pd
from inputFilename import *
from inputNumber import *
from displayMenu import *
from loadData import *
from arrayGrades import *
from roundGrade import *
from gradeMatrix import *
from computeFinalGrades import *
from gradesPlot import *

#-----------------------------------------------------------------------------
# Definitions
#-----------------------------------------------------------------------------

# Data (None = not loaded)
dataRaw = None

# Items for main menu
mainMenu = np.array([
        "Load new data",
        "Check for data errors",
        "Generate plots",
        "Display list of grades",
        "Display statistics",
        "Quit"])

# Items for statistics menu
statisticsMenu = np.array([ 
    "Mean grade of assignment", 
    "Standard deviation of grade in assignment", 
    "Quantile 25%", 
    "Quantile 50%",    
    "Quantile 75%", 
    "Minimum grade", 
    "Maxsimum grade", 
    "Back to main menu"])

# Types of statistics
statistics = np.array([ 
    "mean", 
    "std", 
    "25%", 
    "50%", 
    "75%", 
    "min", 
    "max"])

#-----------------------------------------------------------------------------
# Interactive Grading students program
#-----------------------------------------------------------------------------

while True:
    print("--------------------------------------------------------")
    # If data is not loaded, prompt the user for filename
    if dataRaw is None:
        # Get file name
        filename = inputFilename()
        # Load the raw data from file
        dataRaw = loadData(filename)
        # Selecting grades and counting amount of students and assignments
        gradesArray, students, assignments = arrayGrades(dataRaw)
        print("Number of students: %s" %(students))
        print("Number of assignments: %s" %(assignments))
    
        # Rounding the grades
        validGrades = roundGrade(gradesArray)
        # Reshaping rounded grade array to grade matrix
        matrixGrades = gradeMatrix(validGrades, students)
        # Final grades
        finalGrades = computeFinalGrades(matrixGrades)
        
    # Display menu of options and get chosen menu items
    mainChoice = displayMenu(mainMenu)
    
    #-------------------------------------------------------------------------
    # 1. Load new data
    if mainChoice == 1:
        # Get file name
        filename = inputFilename()
        # Load the raw data from file
        dataRaw = loadData(filename)
        # Selecting grades and counting amount of students and assignments
        gradesArray, students, assignments = arrayGrades(dataRaw)
        print("Number of students: %s" %(students))
        print("Number of assignments: %s" %(assignments))
        
        # Rounding the grades
        validGrades = roundGrade(gradesArray)
        # Reshaping rounded grade array to grade matrix
        matrixGrades = gradeMatrix(validGrades, students)
        # Final grades
        finalGrades = computeFinalGrades(matrixGrades)
    
    #-------------------------------------------------------------------------    
    # 2. Check for data errors    
    elif mainChoice == 2:
        # ERROR MESSAGE 1
        # If two students in the data have the same student id
        studentID = np.array(dataRaw.StudentID)
        if len(np.unique(studentID)) == len(studentID):
            print("All students ID are unique")
        else:
            N = len(np.unique(studentID))
            for i in range(N):
                if np.unique(studentID, return_counts=True)[1][i] == 1:
                    continue
                else:
                    print("%s students in the data have student id: %s" 
                          %(np.unique(studentID, return_counts=True)[1][i],
                            np.unique(studentID, return_counts=True)[0][i]))   
           
        #---------------------------------------------------------------------    
        # ERROR MESSAGE 2
        # If grade in dataset differentiate from the 7-step-scale
        students = np.array(dataRaw)
        count = 0
        for student in students:
            Fail = []
            Mistake = False
            for i in range(len(matrixGrades.T)):
                if np.any(student[i+2] == np.array([-3,0,2,4,7,10,12])):
                    count += 1
                    continue
                else:
                    Fail.append(student[i+2])
                    Mistake = True
            if Mistake == True:
                print("%s has invalid grades: %s" %(student[1], Fail))
        if count == len(matrixGrades) * len(matrixGrades.T):
            print("All given grades are valid")
            
    #-------------------------------------------------------------------------    
    # 3. Generate plots    
    elif mainChoice == 3:
        gradesPlot(np.copy(matrixGrades))
        
    #-------------------------------------------------------------------------    
    # 4. Display list of grades    
    elif mainChoice == 4:
        # Selecting the header and adding a "final grade" column
        # before first assignments
        headings = (dataRaw.columns[2:]).insert(0, "Final Grade")
        
        # Reshaping final grades to fit matrixGrades n:students x m:grades
        matrixFG = finalGrades.reshape(len(finalGrades), 1)
        
        # Merging final grades to the rest of the grades
        allGrades = np.hstack((matrixFG, matrixGrades))
        
        # An overview of grades given to a number of students 
        # in alphabetic order
        display = pd.DataFrame(data = allGrades,
                               index = list((dataRaw.StudentID,dataRaw.Name)),
                               columns = headings).sort_index(level=1)
        
        print(display)
    
    #-------------------------------------------------------------------------    
    # 5. Display statistics   
    elif mainChoice == 5:
        while True:
            print("--------------------------------------------------------")
            # Display menu of options and get chosen menu item
            statisticsChoice = displayMenu(statisticsMenu)            
            #--------------------------------------------------------------
            # 1-7. Compute and display statistic
            if np.any(statisticsChoice == np.array([1, 2, 3, 4, 5, 6, 7])):
                M = int(statisticsChoice)
                statisticResult = display.describe().loc[statistics[M-1]].round(1)
                print(statisticResult.to_string())
            #--------------------------------------------------------------
            # 8. Return to main menu
            elif statisticsChoice == 8:
                break
    
    #-------------------------------------------------------------------------    
    # 6. Quit  
    elif mainChoice == 6:
        print("Goodbye!")
        break