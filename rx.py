# for regular expression
import re

def validate_names(names):
    # Regex pattern for valid names: Firstname Lastname
    pattern = r'^([A-Z][a-z]*\s?){2,3}$'
    for name in names:
        if re.match(pattern, name):
            print(name)
        else:
            print("Wrong name, invalid entry")

# Test the function
names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor Milliken", "Jordan Alexander Williams", "Madonna", "programming is cool"]

validate_names(names)
