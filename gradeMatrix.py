def gradeMatrix(data_array, students):
    # GRADEMATRIX Converting all grades to n x m Matrix
    #
    # Usage:   matrixGrades = gradeMatrix(data_array, students)
    #
    # Input:   grades   An array of grades
    #          students   Number of students in data (int)
    # Output   grade_matrix   n:students x m:grades matrix
    #
    # Author: Nicolai Nisbeth, s175565@student.dtu.dk, 2018
    
    # Computing number of assignments pr. student
    Assignments_pr_student = int(len(data_array) / students)
    
    # Creating an n x m matrix of grades
    grades_matrix = data_array.reshape(students, Assignments_pr_student)
    
    return grades_matrix