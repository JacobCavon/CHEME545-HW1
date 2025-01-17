# CHEME545-HW1
Github repo for my CHEME545 HW1

the `extract_parameter.py` file houses my function for HW1 problem 1:

My approach was to go through all the possible combinations of errors using if statements. For instance, if a unit name doesn't match a key in the dictionary then a warning is returned informing the user of the problem. If neither a unit name nor a parameter name are in the dictionary at all it will inform the user of the problem. The function goes through all possible errors and only returns the output if both the unit name and the parameter name in the nested dictionary accessed by unit name are in the dictionary. Also makes sure that the index is within the range for the list values in the nested dictionary.

the `calculate_solution_weights.py` file houses my function for HW1 problem 2:

Here I initialized an empty list that is returned at the end of the function as the updated list with chemical name, concentration, and weight needed.

I use a for loop to iterate through the whole input list of solutions needed. I extract values from each list item using some code that handles strings, and make sure that I convert items to the appropriate data type (for instance, I needed to convert the concentration string to a float so that I could multiply it by molecular weight). An if statement makes sure that the chemical name is in the dictionary with the molecular weights, and if it is, it appends the string item to the empty list initialized at the top of the function. If the chemical isn't in the molecular weights dictionary then the function appends 'unknown' as an item ot the final list. After iterating through the entire solutions needed list the function returns the new list which included the weight needed.


