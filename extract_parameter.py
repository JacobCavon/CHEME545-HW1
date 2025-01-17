unit_operations_data = {
    "distillation_column": {"temperature": [150, 160, 170], "pressure": [2, 2.5, 3], "flow_rate": [100, 110, 120]},
    "reactor": {"temperature": [250, 260, 270], "pressure": [5, 5.5, 6], "residence_time": [10, 12, 14]},
    "heat_exchanger": {"temperature_in": [80, 90, 100], "temperature_out": [50, 60, 70], "flow_rate": [200, 210, 220]}
}

def extract_parameter(unit_name, parameter_name, index):
    # get all the keys from all the nested dictionaries and collapse them down into a single list
    # this is for the first if statement to check if your parameter name is anywhere in the dict
    all_keys_nested_dict = [list(unit_operations_data[nested_dict].keys()) for nested_dict in unit_operations_data.keys()]
    all_keys_nested_dict_collapsed = sum(all_keys_nested_dict, [])

    # if neither unit name nor parameter name are in the dict then return warning
    if unit_name not in unit_operations_data.keys() and parameter_name not in all_keys_nested_dict_collapsed:
        return f"Your input unit_name '{unit_name}' is not a key in the unit_operations_data dictionary, nor is your input parameter_name '{parameter_name}' anywhere in the dict"

    # return warning if your unit_name isn't in the dict but parameter_name is
    elif unit_name not in unit_operations_data.keys():
        return f"Your input unit_name '{unit_name}' is not a key in the unit_operations_data dictionary"

    # return warning if the parameter name isn't within your nested unit_name dictionary
    elif parameter_name not in unit_operations_data[unit_name].keys():
        return f"Your parameter_name '{parameter_name}' is not in your input unit_name '{unit_name}' dictionary"

    # return warning if your index is out of range for the nested dict value list
    elif unit_name in unit_operations_data.keys() and parameter_name in unit_operations_data[unit_name].keys() and index > (len(unit_operations_data[unit_name][parameter_name])-1):
        return f"Your index is out of range"

    # if everything works return the string w the answer (i.e. if you pass all if statements above)
    else:
        return f'{unit_name}_{parameter_name}_{unit_operations_data[unit_name][parameter_name][index]}'
