import hashlib

def data_sha1(data):
	data = hashlib.sha1(data.encode('utf-8')).hexdigest()
	# print(data)
	return data

def main():
	with open('password.txt', 'r', encoding = 'ISO-8859-1') as f:
		for i in f:
			temp = i.replace('\n','') 
			# print(temp)
			fin = data_sha1(temp)
			print(fin)

if __name__ == '__main__':
	main()
