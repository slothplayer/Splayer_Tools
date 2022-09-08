import pyautogui as pag
import time

# pag.PAUSE = 2
# pag.FAILSAFE = False
fps_60 = 60/1000
mid_x = 735
mid_y = 500


anchor = [mid_x, mid_y, 0, 0]

def test():
	parameter = [-200, -200, 200, 200]
	targer_pic = []
	for i in range(len(anchor)):
		targer_pic.append(anchor[i]+parameter[i]) 

	# print(targer_pic)
	# while(1):
	# 	print(pag.position())
	# 	time.sleep(fps_60)

	# temp = pag.screenshot()

	temp = pag.screenshot(imageFilename = r'./data/temp2.png', region = targer_pic)

	test_1 = None
	while test_1 is None:
		start_time = time.time()
		test_1 = pag.locateOnScreen(r'./data/temp1.png', grayscale = False)
		end_time = time.time()

	print(test_1)
	print( str(round(time.time() - start_time , 3) ) + '秒' )
	# temp.save(r'./data/temp.png')

def main():
	test()

if __name__ == '__main__':
	main()