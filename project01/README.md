# Introduction
The script in this project reads a VCF file and identifies the diseases associated with all the rare variants. The rarity of a variant is determined based on the allele frequencies from the ExAC database. The script counts how many times each of the diseases occur in the file, and displays the information in the console. 

# Pseudocode
```
#!/usr/bin/env python
from pprint import pprint


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

```

# Successes
We completed this project in three separate sessions, where all the members sat down together and talked through the problem at hand while sharing a screen. Hearing everyone's ideas and working off of each other's thoughts helped us arrive to a solution. It was also a good chance for us to learn different programming strategies and techniques from one another, as we had different backgrounds and levels of experience. 

# Struggles
Setting up the GitHub repository at first was somewhat of a struggle. Getting used to the different roles and actions (commit collaborate, merge, fork, etc.) was a little confusing. We had to delete the first one because we had accidentally merged our PR and start branches. However, after some troubleshooting, we were able to create the second repository appropriately. 

# Personal Reflections
## Group Leader
Marcos Equiza Gasco: I had a greta experience working with Hongyuan and Justin. Given this was my first time being team leader (and everyone's first project), we started off a little slow, with some issues in setting up the project repository in GitHub. However, Justin and Hongyuan were both very patient and helpful with fixing up the issue, and together we were able to correctly do it. We met twice outside of classtime, with everyone being very proactive about their schedules, as we wanted to get started early. During the project itself, I led the writing of the pseudo-code and actual code by sharing my screen, but it was a combined effort by all. We didn't encounter any major roadblocks, as we were able to help each other and work through the problem at the same time. As team leader, I tried to organize and run the meetings, but always giving space for Justin and Hongyuan to contribute and share their thoughts. I thought we worked very well as a team, and am happy by the results we got. 

## Other member
Hongyuan Deng：Working with two classmates who are incredibly skilled at coding has been a great experience. I’ve learned so much about coding logic and problem-solving strategies just by observing how they approach a task. Even though coding isn't my strongest suit yet, I made sure to contribute by meticulously checking the details of our code when we writing. I believe that paying close attention to these small details helped us.

Justin Wildman: Working with Hongyuan and Marcos has been a lovely experience. We were fortunately able to meet up twice outside of class to work as a group on the project, which made our communication and brainstorming a lot faster than if we were all doing it on our own time separately. I felt a little bit like I wasn't contributing as much because Marcos was the one doing all the typing when we were planning out our pseudocode and scripting, but I know that we were all doing a lot by bouncing ideas back and forth and walking each other through how we should implement our pseudocode in Python. We didn't have too many roadblocks to get over, as between the three of us, whenever there was something we were't sure how to handle while programming, there was one of us who had a pretty good handle on it. The biggest hurdle we dealt with was getting the github repo working. Our first repo didn't behave correctly, so we spent some time after class separately learning how branches and forks work, which let us come into our first out-of-class session with each of us having a better understanding of how to set up our repo. We did have to relearn pytest together as a gropu when making our test cases, but I wouldn't go so far as to describe that as a roadblock. 

# Generative AI Appendix
No Generative AI was used in this project. 
