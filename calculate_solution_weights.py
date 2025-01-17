molecular_weights = {
    'NaCl': 58.44,
    'H2SO4': 98.079,
    'NaOH': 40.00,
    'KMnO4': 158.034,
    'CH3COOH': 60.052
}

solutions_needed = ['NaCl-0.5M', 'H2SO4-0.25M', 'NaOH-1M', 'KCl-0.1M', 'CH3COOH-0.3M']

def calculate_solution_weights(molecular_weights, solutions_needed):
    # initialize an empty list to store the final list items
    solution_weights_list = []
    
    # iterate through the solutions_needed list
    for i in range(len(solutions_needed)):

        # extract the chemical name and concentration from the list item
        chemical_and_concentration = solutions_needed[i].split('-')
        chemical = chemical_and_concentration[0]
        concentration = float(chemical_and_concentration[1][:-1])
        
        # if the chemical name is in molecular weights then append the chemical name - concentration - weight to the solution_weights_list
        if chemical in molecular_weights.keys():
            # round the float to 2 decimal places
            weight_needed = round(molecular_weights[chemical]*concentration, 2)
            solution_weights_list.append(chemical_and_concentration[0] + '-' + chemical_and_concentration[1] + '-' + str(weight_needed) + 'g')
        
        # if the chemical isn't in molecular weights then append 'unknown' to the solution_weights_list
        else:
            solution_weights_list.append('unknown')
    
    return solution_weights_list
