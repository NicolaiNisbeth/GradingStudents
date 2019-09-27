import numpy as np
from roundGrade import *

def computeFinalGrades(grades):
    # COMPUTEFINALGRADES Calculating the final grade for students in data
    #
    # Usage:   finalGrades = computeFinalGrades(grades)
    #
    # Input:   grades   A matrix of grades on 7-step-scale (integers)
    # Output:   grades   A vector of final grade given to n students(see below)
    #
    # The final grade must be computed in the following way:
    # -Students that have received grade -3, the final grade must be -3.
    # -Students with only one assignment, the final grade must be equal to the
    #  grade of that assignment.
    # -Students with two or more assignments, the final grade is a mean of all 
    #  all grades but the lowest, minus one.
    #
    # Author: Nicolai Nisbeth, s175565@student.dtu.dk, 2018
    
    # Number of students
    N = len(grades)
    
    # Vector containing final grades
    gradesFinal = np.ones(N, dtype=int)
    
    # Loop over grades
    for i in range(N):
        # Takes all grades for i'th student
        student = grades[i]
        
        # Students with grade -3
        if -3 in student:
            gradesFinal[i] = -3
            
        # Students with only one assignment
        elif len(student) == 1:
            gradesFinal[i] = student
            
        # Students with two or more assignments
        elif len(student) > 1:
            # Sorting in descending order and removing furthest to the right
            # Source: stackoverflow: efficiently-sorting-a-numpy-array-in-descending-order
            descending = np.sort(student)[::-1][:-1]
            # Mean of grades
            mean = np.mean(descending)
            # Using roundGrade function to round of the grades
            gradesFinal[i] = roundGrade(np.atleast_1d(mean))
    
    # Returning vector of final grades        
    return gradesFinal