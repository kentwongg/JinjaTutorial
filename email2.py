#!/usr/bin/python

import jinja2

# simple variables
# here is our python dictionary
data = {
    'Popeye\'s Chicken': 'College Street',
    'McDonald\'s': 'Spadina',
    'Chick-Fil-A': 'Yonge St',
    'Nando\'s Chicken': 'Bay St'
}

templateLoader = jinja2.FileSystemLoader(searchpath="templates/")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "email_template.txt"
template_object = templateEnv.get_template(TEMPLATE_FILE)

for k, v in data.items():
    output = template_object.render(store=k, address=v)
    with open("outputs/email_output.txt", "a") as f:
        f.write(output)
        f.write('\n')

# Expected Output
# email_output.txt
# Popeye's Chicken has a 2:1 special at College Street!
# McDonald's has a 2:1 special at Spadina!
# Chick-Fil-A has a 2:1 special at Yonge St!
# Nando's Chicken has a 2:1 special at Bay St!