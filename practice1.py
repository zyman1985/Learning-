from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, sys, random
letter = "GoT"
imgpath = os.path.join(sys.path[0], '111.jpg')
savePath = os.path.splitext(imgpath)

def add_letter(im, wDraw,hDraw):
	font = ImageFont.truetype("Arial.ttf", 30)
	draw = ImageDraw.Draw(im)
#	draw.ellipse(
#		(radioX, radioY, radioX + 70, radioY + 40), fill = "red", outline = "red")
	draw.text((wDraw, hDraw), letter, font = font, fill = "white")
	im.save(savePath[0] +"aa" + ".jpg", "jpeg")
	
if __name__ == "__main__":
	im = Image.open(imgpath)
	w, h = im.size
	print "Original image size: %s x %s" %(w, h)
	wDraw = int(0.9 * w)
	hDraw = int(0.01 * h)
#	radioX = wDraw
#	radioY = hDraw
#	print "radioX:%s" %radioX
#	print "radioY:%s" %radioY
	add_letter(im, wDraw, hDraw)