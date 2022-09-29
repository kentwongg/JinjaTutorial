#!/usr/bin/python
# No Data Model in Python example but now with an external JSON file

import jinja2
import json

# Opening JSON file
f = open('data/email_data.json')
# returns JSON object as
# a dictionary
data = json.load(f)
dict = data['info']
templateLoader = jinja2.FileSystemLoader(searchpath="templates/")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "email_template_jinja_data_structure.txt"
template_object = templateEnv.get_template(TEMPLATE_FILE)

for k, v in dict.items():
    output = template_object.render(store=k, address=v)
    with open("outputs/email_output_json.txt", "a") as f:
        f.write(output)
        f.write('\n')
