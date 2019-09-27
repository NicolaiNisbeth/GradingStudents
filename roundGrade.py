import numpy as np

def roundGrade(grades):
    # ROUNDGRADE Rounds off each element in the vector grades and return
    # the nearest grade on the 7-step-scale.
    #
    # Usage:   validGrades = roundGrade(grades)
    #
    # Input:   grades   A vector of grades (integers)
    # Output:   grades   A vector of rounded grades which are the closest
    #                    numbers on the grading scale.
    #
    # The data can be any given number, in case of a number being inbetween
    # two given grades on the 7-step-scale, the higher grade will be chosen.
    #
    # Author: Nicolai Nisbeth, s175565@student.dtu.dk, 2018

    # Number of grades
    N = len(grades)
    
    # 7-step-scale
    step_scale = np.array([-3, 0, 2, 4, 7, 10, 12])
    
    # Vector containing valid grades
    gradesRounded = np.zeros(N, dtype=int)
    # Loop over all grades
    for i in range(N):
        # If grade is valid append else find the closest corresponding grade 
        # on 7-step-scale
        if grades[i] in step_scale:
            gradesRounded[i] = grades[i]
        else:
            # Computing the difference between selected grade and grade system
            delta = abs(np.array([grades[i] - x for x in step_scale]))
            # Getting position of the smallest index
            index_min = np.argmin(delta)
            # Selecting and inserting grade according to position number
            gradesRounded[i] = step_scale[index_min]
        
    # Return valid grades on 7-step-scale    
    return gradesRounded