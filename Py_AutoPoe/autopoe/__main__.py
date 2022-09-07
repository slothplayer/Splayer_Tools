import pyautogui as pag
import time

# pag.PAUSE = 2
pag.FAILSAFE = False
fps_60 = 60/1000

def test():
	# while(1):
	# 	print(pag.position())
	# 	time.sleep(fps_60)

	temp = pag.screenshot()
	temp.save(r'./data/temp.jpg')

def main():
	test()

if __name__ == '__main__':
	main()