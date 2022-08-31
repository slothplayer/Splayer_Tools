import os
import pandas as pd
import xlsxwriter

def data_analysis(data):
	123


def main():
	path = os.getcwd() + "/test/"
	
	cur_have_list = []
	for i in os.listdir(path):
		cur_have_list.append( i[ i.find(r".") -3 : i.find("_V") ].strip(r"_") )
	
	# print(cur_have_list)
	
	target_list = []
	with open("target.txt") as f:
		for line in f.readlines():
			target_list.append(line.strip("\n"))

	# print(target_list)
	
	list_notin = list( set(cur_have_list).difference(set(target_list) ))
	list_notin.sort()
	print( list_notin )
	with open("Notin.txt" , "w") as f:
		for i in list_notin:
			f.write("%s\n" % i)

	print( list( set(target_list).difference(set(cur_have_list) )) )



if __name__ == "__main__":
	main()