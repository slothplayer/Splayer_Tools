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
	print(targer_pic)
	# while(1):
	# 	print(pag.position())
	# 	time.sleep(fps_60)

	# temp = pag.screenshot()
	temp = pag.screenshot(imageFilename = r'./data/temp1.png', region = targer_pic)
	# temp.save(r'./data/temp.png')

def main():
	test()

if __name__ == '__main__':
	main()