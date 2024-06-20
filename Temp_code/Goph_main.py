import pandas as pd
import os
import xlsxwriter
import json
import datetime

def data_details_clear(data):
	arr_addr = []
	arr_user = []

	for i in data['details']:
		addr = ''
		user = ''
		if type(i) != float:
			i = json.loads(i)
			i = i.get('browser')

			addr = i.get('address')
			user = i.get('user-agent')

		arr_addr.append(addr)
		arr_user.append(user)

	data.loc[:,'addr'] = arr_addr
	data.loc[:,'user_agent'] = arr_user
	
	
	return data

def data_time_clear(data):
	temp = data

	arr_time = []
	for i in temp['time']:
		UTC_FORMAT = '%Y-%m-%dT%H:%M:%S'
		utc_time = datetime.datetime.strptime(i.split('.')[0], UTC_FORMAT)
		localtime = utc_time + datetime.timedelta(hours = 8)
		
		arr_time.append(localtime)

	temp['time'] = arr_time
	temp = temp.assign(s_time = '')

	for i,j in temp.iterrows():
		if type(j['email']) != float:
			if str(temp.loc[ i,'s_time']) == '':
				temp.loc[ temp.email == j['email'],'s_time'] = j['time']

	data = temp
	return data

def csv_merge(in_path):
	path = in_path

	temp = pd.DataFrame()
	for i in os.listdir(path):
		if '.csv' in i:
			file = pd.read_csv(path+"/"+i , encoding = 'ISO-8859-1')
			
			# data clear
			file = data_details_clear(file)
			file = data_time_clear(file)
			# file = data_message_clear(file)
			# file = data_drop_clear(file)

			temp = pd.concat([temp,file],axis = 0)
		
	temp.drop(['details'], axis = 1,inplace = True)
	temp = temp[temp['message'] != 'Email Sent']
	# temp.drop_duplicates(inplace = True)
	temp = temp[['email', 's_time', 'time', 'message', 'addr', 'user_agent', 'campaign_id']]
	# temp = temp.append(temp.loc[temp['user_agent'].str.contains('GoogleImageProxy'),:])
	# temp = temp.drop_duplicates(keep=False)
	# print(temp)
	return temp

def attribute_trans(data, format_list):
	temp = data
	
	list_attri = []
	list_trans = []
	for i,j in format_list.iterrows():
		list_attri.append(j[0])
		list_trans.append(j[1])
	
	attri_trans = zip(list_attri, list_trans)
	temp.rename(columns = dict(attri_trans), inplace = True)

	data = temp
	return data

def campain_merge(data,c_list):
	temp = data

	campains_list = pd.read_excel(c_list)
	temp = pd.merge(temp, campains_list, how='left')

	# ['campaign_id', '範本名稱', '附件名稱', '釣魚連結位址']
	c_data = temp[['campaign_id', '範本名稱', '附件名稱', '釣魚連結位址']]
	c_data = pd.concat([campains_list,c_data],axis = 0)
	c_data = c_data.drop_duplicates()
	
	c_data.to_excel(c_list, index=False)

	data = temp.drop(['campaign_id'], axis = 1)
	return data

def main():
	path_csv = os.getcwd() + '/Csv/'
	path_format = os.getcwd() + '/Format/'
	path_property = os.getcwd() + '/Property/'
	path_campain = os.getcwd() + '/Campain/'

	raw_data = csv_merge(path_csv)
	# ['email', 'time', 'message', 'details', 'addr', 'user_agent', 'campaign_id'] 
	
	property_list = pd.read_excel(path_property + 'Target.xlsx')
	# property_list.rename(columns = {'Email Address' : 'email'}, inplace = True)
	
	data_property = pd.merge(property_list,raw_data)
	
	data_final = campain_merge(data_property, path_campain + 'Campains.xlsx' )

	format_list = pd.read_excel(path_format + 'Format.xlsx', header = None)

	Final = attribute_trans(data_final, format_list)

	Final.to_excel('output.xlsx', index=False)


if __name__ == '__main__':
	main()