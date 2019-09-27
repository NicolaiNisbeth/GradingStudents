import pandas as pd
import numpy as np

def loadData(filename):
    # LOADDATA Loads the filename.
    #
    # Usage:   dataRaw = loadData(filename)
    #
    # Input:   filename   Filename of CSV file (string)
    # Output:   dataRaw   Dataset loaded in python (see below)
    #
    # If a student has grades missing these will be replaced with the default
    # grade: -3 and user will be informed.
    # In case an other grade is desired the user is welcome to fill out empty
    # grades with the desired grade before loading the data.
    #
    # If a studentID is missing fill it with: sXXXXXX
    # If a name is missing fill it with: Unknown
    #
    # Author: Nicolai Nisbeth, s175565@student.dtu.dk, 2018
    
    # Loading CSV file
    data = pd.read_csv(filename)
    
    # Replacing missing data in dataset
    if np.any(pd.isnull(data) == True):
        values = {"StudentID": "sXXXXXX", 
                  "Name": "Unknown"}
        data = data.fillna(value=values)
        if np.any(pd.isnull(data) == True):
            print("Missing grades were found in dataset and will be assigned default grade: -3")
            data = data.fillna(value = -3)
    return data