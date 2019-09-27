import numpy as np
import matplotlib.pyplot as plt
from computeFinalGrades import *

# Getting rid of matplotlib.mpl warning
# Source: stackoverflow:python-matplotlib-getting-rid-of-matplotlib-mpl-warning
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)

def gradesPlot(grades):
    # GRADESPLOT Converting all grades to two plots:
    #            1) Bar plot of final grades
    #            2) Scatter plot of given grades for assignments
    #
    # Usage:   gradesplot(grades)
    #
    # Input:   grades   A matrix of grades on 7-step-scale
    #
    # Author: Nicolai Nisbeth, s175565@student.dtu.dk, 2018
    
    # 7-step-scale
    step_scale = np.array([12,10,7,4,2,0,-3])
    
    # Using computeFinalGrades function to compute final grade for 
    # each student
    finalGrade = computeFinalGrades(grades)
    
    # Frequency of unique final grade
    axis_x, axis_y = np.unique(finalGrade, return_counts=True)
    
    # Figure: Final grades
    # Bar plot
    plt.bar(axis_x, axis_y, align='center', alpha=1)
    
    # Title and axis labels
    plt.title("Overview of final grade given to students")
    plt.xlabel("7-step-scale")
    plt.ylabel("Frequency")
    
    # Tick-labels
    plt.xticks(step_scale)
    plt.yticks(axis_y)
    
    # Show plot
    plt.show()
    
    #-------------------------------------------------------------------------
    # Figure: Grades per assignment
    # Diagram consisting of following:
    #   1. Each given grade is marked by a dot
    #   2. Average grade for each of the assignments
    
    # Freq_Students and Freq_Assignments
    Freq_S, Freq_A = len(grades), len(grades.T)
    
    # y-axis
    GradesNumber = []
    # x-axis
    AssignmentNumber = []
    # Label for x-axis 
    AssignmentName = []
    
    # 1.
    # Extracting coordinates by looping over assignments
    for i in range(Freq_A): 
        # All grades for i'th assignment
        GradesNumber.append(np.array([float(x) for x in grades[:,i]]))
        # Assignment Number i'th
        AssignmentNumber.append(i+1)
        # Assignment Name i'th
        AssignmentName.append("Assignment %s" %(i+1))
     
    # Adding a small random number to seperate the dots which would
    # otherwise be stacked on top of each other
    for i in range(Freq_A):
        variation = np.random.uniform(-0.1,0.1 , Freq_S)
        GradesNumber[i] += variation
    
    # Plot grades for each assignment seperately    
    # Source: stackoverflow python-scatter-plot-with-multiple-y-values-for-each-x
    for x, y in zip(AssignmentNumber, GradesNumber):
        plt.scatter(x+variation, y, alpha=1, marker=".", s=30)

    #-------------------------------------------------------------------------
    # 2.
    # Mean grade for each assignment
    Assignment_grade_mean = np.mean(GradesNumber, axis=1)
    
    # Plot average grade for each assignment as a line
    if len(AssignmentNumber) == 1:
        plt.plot(AssignmentNumber,Assignment_grade_mean, 
                 "r*", alpha=1, label="Average grade")
    else:
        plt.plot(AssignmentNumber,Assignment_grade_mean, 
                 "r-", alpha=0.5, label="Average grade")
        
    # Title and axis labels
    plt.title("Grades given in assignment")
    plt.axes().set_xticklabels([x for x in AssignmentName], rotation=90)
    plt.xticks(AssignmentNumber)
    plt.ylabel("7-step-scale")
    plt.yticks(np.arange(-3,13), 
              ("-3","","","0","","2","","4","","","7","","","10","","12"))
    
    # Legend
    plt.legend(bbox_to_anchor=(1.02, 1), loc=2, borderaxespad=0)
    
    # Show plot
    plt.show()