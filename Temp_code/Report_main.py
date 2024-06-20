import pandas as pd
import os
import xlsxwriter

class Report_maker():
	def __init__(self):#完成
		self._data_path = r"./Nessus" # nessus的csv檔案位置(資料夾)
		self._data_plugin = r"./Plugin/Plugin.xlsx" # plugin的檔案位置(檔案)
		self._data_ip = r"./IP/IP.xlsx" # 目標IP(檔案)

		self._file_path = r"./Final" #最後檔案的位址(資料夾)
		self._file_name = r"Data.xlsx" #最後檔案的名子(檔案)
				
		self._report_format = [
			"Host","Risk","Name",
			"弱點描述","處理方式說明",
			"Plugin ID","Protocol",
			"CVSS v2.0 Base Score",
			"Port","CVE","Plugin Output",
			]
		# 表二後半的欄位名稱
		
		# 表單名稱
		self._sheet_1_name = r"掃描清單"
		self._sheet_2_name = r"各主機弱點列表"
		self._sheet_3_name = r"掃描結果"
		self._sheet_4_name = r"各弱點數量統計"
		self._sheet_5_name = r"TOP 20高風險IP"
		self._sheet_6_name = r"TOP 20弱點數量IP"

	def nassue_data(self):#完成
		path = self._data_path
		file_list = list()
		for i in os.listdir(path):
			temp = i+".csv"
			file_list.append(i)

		temp = pd.DataFrame()
		for i in file_list:
			file = pd.read_csv(path+"/"+i , encoding = 'ISO-8859-1')
			temp = pd.concat([temp,file],axis = 0)

		# temp.drop(["Port","CVE","Plugin Output"], axis=1,inplace=True)
		temp.drop_duplicates(inplace = True)
		return temp

	def delete_last(self):#完成
		try:
			os.remove(self._file_path + "/" + self._file_name )	
		except OSError:
			pass

	def do_report(self):#完成
		self.delete_last()
		self.data_analysis()
		self.make_excel()

	def make_excel(self):#完成
		writer = pd.ExcelWriter(self._file_path+"/"+self._file_name)
		self._sheet_1.to_excel(writer, sheet_name = self._sheet_1_name ,index = False)
		self._sheet_2.to_excel(writer, sheet_name = self._sheet_2_name ,index = False)
		self._sheet_3.to_excel(writer, sheet_name = self._sheet_3_name ,index = False)
		self._sheet_4.to_excel(writer, sheet_name = self._sheet_4_name ,index = False)
		self._sheet_5.to_excel(writer, sheet_name = self._sheet_5_name ,index = False)
		self._sheet_6.to_excel(writer, sheet_name = self._sheet_6_name ,index = False)
		writer.save() #完成

	def data_analysis(self):#完成
		self._sheet_1 = self.sheet_1()
		self._sheet_2 = self.sheet_2(self.nassue_data())
		self._sheet_3 = self.sheet_3(self._sheet_2)
		self._sheet_4 = self.sheet_4(self._sheet_2)
		self._sheet_5 = self.sheet_5(self._sheet_3)
		self._sheet_6 = self.sheet_6(self._sheet_3) 

	def sheet_1(self): #完成
		temp = pd.read_excel(self._data_ip,sheet_name = None)
		temp = temp.get(self._sheet_1_name)
		temp.drop_duplicates(inplace = True)
		# 過濾格式
		return temp 
		
	def sheet_2(self,data):#完成
		plugin_df = pd.read_excel(self._data_plugin)		

		temp = pd.merge(data,plugin_df,how = "left",on = "Plugin ID").reset_index(drop = True)
		temp.loc[temp["弱點描述"].isnull(),"弱點描述"] = temp.Description
		temp.loc[temp["處理方式說明"].isnull(),"處理方式說明"] = temp.Solution


		tar = temp["Host"].to_list()
		self._sheet_1["掃描狀況"] = self._sheet_1["IP"].isin(tar).replace(
			[True,False],
			["V","X"],
			)

		temp = temp[temp["Risk"] != "None"]
		temp = temp[self._report_format]
		temp.rename(columns = {"Host":"IP","Risk":"Level"},inplace = True)
		final = pd.merge(self._sheet_1,temp,on = "IP").reset_index(drop = True) #how = "right"

		return final	

	def sheet_3(self,s_1):#完成
		data_va = s_1

		temp = data_va[ ["IP","Level"] ]
		new_df = pd.DataFrame(columns = ["IP","C","H","M","L","Total"])
		for i in temp["IP"].drop_duplicates():	
			C = temp[ (temp.IP == i) & (temp.Level == "Critical") ].Level.count()
			H = temp[ (temp.IP == i) & (temp.Level == "High") ].Level.count()
			M = temp[ (temp.IP == i) & (temp.Level == "Medium") ].Level.count()
			L = temp[ (temp.IP == i) & (temp.Level == "Low") ].Level.count()
			
			new_df = new_df.append({
				"IP" : i,"C" : C,
				"H" : H,"M" : M,"L" : L,
				"Total" : (C+H+M+L)},
				ignore_index = True
				)

		final = pd.merge(self._sheet_1,new_df,how = "left",on = "IP").reset_index(drop = True)
		final.rename(columns = {
			"C":"嚴重風險數量","H":"高風險數量",
			"M":"中風險數量","L":"低風險數量",
			"Total":"弱點總數"},
			inplace = True
			)
		
		return final

	def sheet_4(self,data):#完成
		data_va = data
		new_df = pd.DataFrame(columns = ["Level","Name","Count","IP"])

		for i in data_va["Name"].drop_duplicates():
			data_count = data_va[ (data_va.Name == i)].IP.count()
			data_level = data_va[ (data_va.Name == i)].drop_duplicates("Level").reset_index(drop = True)

			new_df = new_df.append({
				"Level" : data_level.loc[0,"Level"],
				"Name" : i,
				"Count" : data_count,
				"IP" : ",".join([x for x in data_va[ (data_va.Name == i)].IP.drop_duplicates()])},
				ignore_index = True
				)

		sorter = ["Critical","High","Medium","Low"]
		new_df.Level = new_df.Level.astype("category")
		new_df.Level.cat.set_categories(sorter,inplace = True)
		final = new_df.sort_values(by =["Level","Count"],ascending = [True , False]).reset_index(drop = True)
		final.rename(columns = {
			"Level":"弱點等級",
			"Name":"弱點名稱",
			"Count":"觸發弱點數量",
			"IP":"觸發IP"},
			inplace = True
			)

		return final

	def sheet_5(self,data):#完成
		temp = data[["IP","嚴重風險數量","高風險數量"]]
		temp["Sum"] = temp.loc[:,["嚴重風險數量","高風險數量"]].sum(axis = 1).astype(int)
		final = temp[["IP","Sum"]]
		final = pd.merge(self._sheet_1,final,how = "right",on = "IP").reset_index(drop = True)
		final = final.drop_duplicates()
		final = final.sort_values(by = ["Sum"] , ascending = False).reset_index(drop = True).head(20)
		final.rename(columns = {"Sum":"高風險弱點數量"},inplace = True)
		
		return final

	def sheet_6(self,data):#完成
		temp = data[["IP","嚴重風險數量","高風險數量","中風險數量","低風險數量"]]
		temp["Sum"] = temp.loc[:,["嚴重風險數量","高風險數量","中風險數量","低風險數量"]].sum(axis = 1).astype(int)
		final = temp[["IP","Sum"]]
		final = pd.merge(self._sheet_1,final,how = "right",on = "IP").reset_index(drop = True)
		final = final.drop_duplicates()
		final = final.sort_values(by = ["Sum"] , ascending = False).reset_index(drop = True).head(20)
		final.rename(columns = {"Sum":"弱點數量"},inplace = True)
		
		return final 

def main():
	test = Report_maker()
	test.do_report()

if __name__ == "__main__":
	main()
