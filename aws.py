#!/usr/bin/python
# AWS example

import jinja2
import json

# Opening JSON file
f = open('data/aws_data.json')
# returns JSON object as
# a dictionary
data = json.load(f)
dict = data['cfn']
templateLoader = jinja2.FileSystemLoader(searchpath="templates/")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "aws.yaml"
template_object = templateEnv.get_template(TEMPLATE_FILE)

output = template_object.render(data=dict)
with open("outputs/cloudformation_artifact.yaml", "a") as f:
    f.write(output)
    f.write('\n')
