import pandas as pd
import json

def data_clean(data):
	for i in data['user_group_list']:
		print(repr(i['name']))
	return data

def main():
	with open('test.json','r') as f:
		data = json.load(f)
		# print(data)
		# json_data = pd.read_json(text, orient ='index')
		data_clean(data)
		# temp_str = "123123123"

if __name__ == '__main__':
	main()
