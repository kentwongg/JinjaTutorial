#!/usr/bin/python

from jinja2 import Template

# simple variables
store = 'Popeye\'s Chicken'
address = 'College Street'
# creating a jinja object
template_object = Template("{{ store }} has a 2:1 special at {{ address }}!")
output = template_object.render(store=store, address=address)
# print to console
print(output)
