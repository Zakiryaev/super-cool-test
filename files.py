import os
import csv
import json


print('' '')

target_dir = 'projects'
os.chdir('/Users/egorzakiryaev/projects')


one_more_new_user = {
    'first_name': 'Alexanre',
    'last_name': 'Moraru',
    'article': '32',
    'book': ['Chisinau']
}


with open('/Users/egorzakiryaev/projects/ecom/text.txt', 'w') as f:
          f.write (json.dumps(one_more_new_user,))
