from PIL import Image, ImageFilter
from PIL.ImageFilter import(BLUR, CONTOUR, EDGE_ENHANCE, EDGE_ENHANCE_MORE, EMBOSS, FIND_EDGES, SHARPEN)



def sharpenImage(curImg, counter):
	current = Image.open(curImg)
	newImg = current.filter(SHARPEN)
	newImg.save('image' + str(counter) + '.jpg')


def blurImage(curImg, counter):
	current = Image.open(curImg)
	newImg = current.filter(BLUR)
	newImg.save('image' + str(counter) + '.jpg')


def rotateCounter(curImg, counter):
	newImg = Image.open(curImg)
	newImg.rotate(90).save('image' + str(counter) + '.jpg')


def rotateClockwise(curImg, counter):
	newImg = Image.open(curImg)
	newImg.rotate(270).save('image' + str(counter) + '.jpg')


def cropImage(curImg, counter):
	current = Image.open(curImg)
	width, height = current.size
	left = width / 3
	top = height / 3
	right = 3 * width / 4
	bottom = 3 * height / 4
	newImg = current.crop((left, top, right, bottom))
	newImg.save('image' + str(counter) + '.jpg')


def sketchImage(curImg, counter):
	current = Image.open(curImg)
	newImg = current.filter(CONTOUR)
	newImg.save('image' + str(counter) + '.jpg')



def oilImage(curImg, counter):
	current = Image.open(curImg)
	newImg = current.filter(EDGE_ENHANCE)
	newImg.save('image' + str(counter) + '.jpg')


def pencilImage(curImg, counter):
	current.Image.open(curImg)
	newImg = current.filter(EDGE_ENHANCE_MORE)
	newImg.save('image' + str(counter) + '.jpg')



def foilImage(curImg, counter):
	current = Image.open(curImg)
	newImg = current.filter(EMBOSS)
	newImg.save('image' + str(counter) + '.jpg')



def negativeImage(curImg, counter):
	current = Image.open(curImg)
	newImg = current.filter(FIND_EDGES)
	newImg.save('image' + str(counter) + '.jpg')
