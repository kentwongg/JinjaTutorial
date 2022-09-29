#!/usr/bin/python

from jinja2 import Template

# simple variables
# here is our python dictionary
data = {
    'Popeye\'s Chicken': 'College Street',
    'McDonald\'s': 'Spadina',
    'Chick-Fil-A': 'Yonge St',
    'Nando\'s Chicken': 'Bay St'
}
# creating a jinja object
template_object = Template("{{ store }} has a 2:1 special at {{ address }}!")
# use a simple for loop to iterate through the data dictionary we have
for k, v in data.items():
    output = template_object.render(store=k, address=v)
    # print to console
    print(output)
