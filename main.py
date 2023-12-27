from PIL import Image
import numpy as np
import cv2
import time
import os
def colour(r, g, b):
	return f"\x1b[48;2;{r};{g};{b}m"+" " + "\x1b[0m"

def render_image(img):
	print("\n".join(map(lambda line:"".join(list(map(lambda char:colour(char[2], char[1], char[0]), line))), img))) #damn crazy one liner

terminal_size = os.get_terminal_size()
path = "./sample.mp4" #path to ur video
video = cv2.VideoCapture(path) #change to this line to play a video file
#video = cv2.VideoCapture(0)#change to this line to display camera
fps = video.get(cv2.CAP_PROP_FPS)
ret = True
while ret:
	ret, img = video.read()
	if ret:
		img = Image.fromarray(img)
		img = img.resize((terminal_size[0], terminal_size[1]+1))
		render_image(np.asarray(img))
	time.sleep(1/fps)
