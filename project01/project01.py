#!/usr/bin/env python
from pprint import pprint


# Modify this function signature and fill in the details
def parse_line(line: str, rare_variant_threshold: float):

    # Split line by tab to separate fields

    # Access last index of split (INFO field) --> store as info variable (str)

    # Split info by ; --> each index is a key-value pair separated by = --> store as key_value_pairs variable (list)

    # Split key-value pairs by =, and make dictionary key_value_dict {key: values}
    # Key is first index, values are second index --> {key: strings}

    # Make split_dict dictionary for splitting
    # {"AF_EXAC": ',', "CLNDN": '|'}

    # Access "AF_EXAC" key in key_value_dict 
        # If error --> exit function (move on to next line)
        # Set is_rare = FALSE
        # Split values using split_dict delimiter
        # Iterate over values from "AF_EXAC"
            # Convert to float and compare with rare_variant_threshold
            # If FALSE --> continue to next value
            # If any values meet threshold (< than threshold), set is_rare = TRUE --> break
            # If is_rare = FALSE at the end of loop --> return []
    
    # At this point, we have identified a rare variant
    
    # Access "CLNDN" key in key_value_dict and split by split_dict delimiter
    # If "not_provided" or "not_specified" in the list, remove them 
    # Return list of diseases
    
    pass


# Modify this function signature and fill in the details
def read_file(file: str):

    # Create disease_count dictinary for running tally

    # Open and read file

    # Check if line starts with #, if it does -> ignore
    # If it doesn't --> run parse_line() --> store in diseases variable

    # Iterate through items in diseases
    # If disease (key) in disease_count dict --> +1 to value
    # Else create new key --> set 1 as value

    # disease_count[disease] = disease_count.get(disease, 0) + 1

    # return disease_count

    pass


if __name__ == "__main__":
    pprint(read_file("clinvar_20190923_short.vcf"))
