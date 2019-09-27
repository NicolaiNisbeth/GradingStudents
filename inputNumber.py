def inputNumber(prompt):
    # INPUTNUMBER Prompts user to input a number. Repeats until valid number.
    #
    # Usage: number = inputNumber(prompt) 
    #
    # Author: From "Creating an interactive menu" made by Mikkel N. Schmidt.
    
    # Checks if user input is a number    
    while True:
        try:
            number = float(input(prompt))
            break
        except ValueError:
            pass
    return number