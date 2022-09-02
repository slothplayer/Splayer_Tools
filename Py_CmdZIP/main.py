# zip -er foo.zip foo -x "*.DS_Store"
import os

targer_path = os.getcwd()
zip_cmd = ""

for i in os.listdir(targer_path):
	zip_cmd = ''
	if i == 'main.py' or i == '.DS_Store' or i == 'run_py.command':
		continue
	else:
		zip_cmd += 'zip -er {}.zip {} '.format(i,i)

	zip_cmd +=  r'-x "*.DS_Store" -x "__MACOSX"'

	print('file : {} >>>> {}.zip '.format(i,i))
	# print(zip_cmd)
	os.system(zip_cmd)