import requests

class Http_requests(object):
	def __init__(self):
		super(Http_requests, self).__init__()

		self.target = ''
		self.data = {'name':'123'}
		self.auth = {'',''}

	def Http_post(self,target):
		r = requests.post(
			target,
			auth= self.auth,
			data= self.data
		)
		# print(r.text[index_start:index_end])
		print(r.text)
		# print(r.cookies)

def main():
	test = Http_requests()

if __name__ == '__main__':
	main()