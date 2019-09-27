import numpy as np

def arrayGrades(data):
    # ARRAYGRADES Converting all grades in data to an array
    #
    # Usage:   gradesArray,students,assignments = arrayGrades(data)
    #
    # Input:   data   CSV file containing grades given to n students (see below)
    # Output:   gradesArray   An array of given grades (integer)
    #           students      Number of students (integer)
    #           assignments   Number of assignments (integer)
    #
    # Data format: The first row in CSV file contains the column headings.
    #              Each of the following rows contains a:
    #              studentID | name | n grade for m assignments 
    #
    # Author: Nicolai Nisbeth, s175565@student.dtu.dk, 2018
    
    # Selecting grades in data
    grades = np.array(data.iloc[:, 2:])
    
    # Amount of students and assignments in data
    students, assignments = len(grades), len(grades.T)
    
    # Converting grades to one long array
    grades_array = grades.ravel()
    
    return grades_array, students, assignments