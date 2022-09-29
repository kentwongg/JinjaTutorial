#!/usr/bin/python
# No Data Model in Python example

import jinja2

# No data Model here

templateLoader = jinja2.FileSystemLoader(searchpath="templates/")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "email_template_jinja_data_structure.txt"
template_object = templateEnv.get_template(TEMPLATE_FILE)


output = template_object.render()
with open("outputs/email_output_jinja_data_structure.txt", "a") as f:
    f.write(output)
    f.write('\n')

