#!/usr/bin/env python
from pprint import pprint


def parse_line(line: str, rare_variant_threshold: float = 0.0001):

    # Split line by tab to separate fields
    line = line.strip().split('\t')

    # Access last index of split (INFO field) --> store as info variable (str)
    info = line[-1]

    # Split info by ; --> each index is a key-value pair separated by = --> store as key_value_pairs variable (list)
    key_value_pairs = info.split(';')

    # Split key-value pairs by =, and make dictionary key_value_dict {key: values}
    # Key is first index, values are second index --> {key: strings}
    key_value_dict = {}
    for kv in key_value_pairs:
        kv = kv.split('=')
        key_value_dict[kv[0]] = kv[1]

    # Make split_dict dictionary for splitting
    # {"AF_EXAC": ',', "CLNDN": '|'}
    split_dict = {"AF_EXAC": ',', "CLNDN": '|'}

    # Access "AF_EXAC" key in key_value_dict 
    try:
        af_exac = key_value_dict['AF_EXAC']
    # If error --> exit function (move on to next line)    
    except KeyError as err:
        print(f"Key doesn't exist {err}")
        return []
    
    # Set is_rare = FALSE    
    is_rare = False

    # Split values using split_dict delimiter
    af_exac = af_exac.split(split_dict["AF_EXAC"])
        
    # Iterate over values from "AF_EXAC"
    for value in af_exac:

        # Convert to float and compare with rare_variant_threshold
        # If any values meet threshold (< than threshold), set is_rare = TRUE --> break
        if float(value) < rare_variant_threshold:
            is_rare = True
            break

        # If FALSE --> continue to next value
        else:
            continue

    # If is_rare = FALSE at the end of loop --> return []
    if not is_rare:
        return []
            
    # At this point, we have identified a rare variant
    
    # Access "CLNDN" key in key_value_dict and split by split_dict delimiter
    clndn = key_value_dict["CLNDN"].split(split_dict['CLNDN'])

    # If "not_provided" or "not_specified" in the list, remove them 
    try:
        clndn.remove('not_provided')
    except ValueError as err:
        pass

    try:
        clndn.remove('not_specified')
    except ValueError as err:
        pass

    # Return list of diseases
    return clndn


def read_file(file: str):

    # Create disease_count dictinary for running tally
    disease_count = dict()

    # Open and read file
    with open(file, 'r') as f:
        while True:

            line = f.readline()

            # Check if line is empty (end of file)
            if line == '':
                break

            # Check if line starts with #, if it does -> ignore
            elif line[0] == '#':
                continue

            # If it doesn't --> run parse_line() --> store in diseases variable (list)
            else:
                diseases = parse_line(line)

                # Iterate through items in diseases
                # If disease (key) in disease_count dict --> +1 to value
                # Else create new key --> set 1 as value
                for disease in diseases:
                    disease_count[disease] = disease_count.get(disease, 0) + 1

    return disease_count


if __name__ == "__main__":
    pprint(read_file("clinvar_20190923_short.vcf"))
