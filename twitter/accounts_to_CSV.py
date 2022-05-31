#!/bin/python

import json

with open('accounts.json') as json_file:
	author_data = json.load(json_file)

with open('author.csv', 'w') as f:
	for author, a_data in author_data.items():
		f.write(f"{a_data['username']};{author};" + str({a_data['description'].replace('\n','//')}) + f";{a_data['public_metrics']['followers_count']}\n")