import glob
import ast
import csv
from collections import OrderedDict

file_list = glob.glob('*.txt')
with open(file_list[0], 'r') as file:
    content = file.read()
    raw_data = list(ast.literal_eval(content))
    
    format = ['Number', 'Name', 'Website', 'Phone', 'Address', 'Owner', 'Youtube', 'Instagram', 'Twitter', 'Linkedin', 'Reddit', 'Tiktok', 'Mail', 'Facebook']

    company_data = []
    for company in raw_data:
        company_data.append(OrderedDict((key, company.get(key)) for key in format))
    filename = "companies.csv"

    # writing to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=format)
    
        # writing headers (field names)
        writer.writeheader()
    
        # writing data rows
        writer.writerows(company_data)