from tkinter import *
from PIL import Image, ImageTk
from editFunctions import sharpenImage, blurImage, rotateCounter
from editFunctions import rotateClockwise, cropImage, sketchImage, oilImage, pencilImage, foilImage, negativeImage


def changeImage(counter):
	img = ImageTk.PhotoImage(Image.open('image' + str(counter) +'.jpg'))
	panel.configure(image = img)
	panel.image = img


def sharpenImageFunction():
	global rotateCounter
	curImg = 'image' + str(counter) + '.jpg'
	counter = counter + 1
	sharpenImage(curImg, counter)
	changeImage(counter)


def blurImageFunction():
	global counter
	curImg = 'image' + str(counter) + '.jpg'
	counter = counter + 1
	blurImage(curImg, counter)
	changeImage(counter)

def rotateCounterFunction():
	global counter
	curImg = 'image' + str(counter) + '.jpg'
	counter = counter + 1
	rotateCounter(curImg, counter)
	changeImage(counter)


def rotareClockwiseFunction():
	global counter
	curImg = 'image' + str(counter) + '.jpg'
	counter = counter + 1
	rotateClockwise(curImg, counter)
	changeImage(counter)


def cropImageFunction():
	global counter
	curImg = 'image' + str(counter) + '.jpg'
	counter = counter + 1
	cropImage(curImg, counter)
	changeImage(counter)


def undoFunction():
	global counter
	if counter > 0:
		counter = counter - 1
	changeImage(counter)


def sketchImageFunction():
	global counter 
	curImg = 'image' + str(counter) + '.jpg'
	counter = counter + 1
	sketchImage(curImg, counter)
	changeImage(counter)


def oilImageFunction():
	global counter
	curImg = 'image' + str(counter) + '.jpg'
	counter = counter + 1
	oilImage(curImg, counter)
	changeImage(counter)


def paintImageFunction():
	global counter 
	curImg = 'image' + str(counter) + '.jpg'
	counter = counter + 1
	pencilImage(curImg, counter)
	changeImage(counter)


def foilImageFunction():
	global counter 
	curImg = 'image' + str(counter) + '.jpg'
	counter = counter + 1
	foilImage(curImg, counter)
	changeImage(counter)


def negativeImageFunction():
	global counter 
	curImg = 'image' + str(counter) + '.jpg'
	counter = counter + 1
	negativeImage(curImg, counter)
	changeImage(counter)


main = Tk()
counter = 0
main.title("Photo Editor")
main.geometry("1000x505")
var = IntVar()
editingBox = Frame(main)


undoButton = Button(main, text="Undo", command=undoFunction, font=20)
undoButton.pack(side=BOTTOM, pady=10)

formatLabel = Label(editingBox, text = "Format", font=16)
formatLabel.pack(side = TOP, pady=10)

sharpenButton = Button(editingBox, text = "Sharpen Image", command=sharpenImageFunction, width=20)
sharpenButton.pack(side = TOP)

blurButton = Button(editingBox, text="Blur Image", command=blurImageFunction, width=20)
blurButton.pack(side = TOP)

cropButton = Button(editingBox, text="Crop", command=cropImageFunction, width=20)
cropButton.pack(side = TOP)

rotateCounterButton = Button(editingBox, text="Rotate Counter Clockwise", command = rotateCounterFunction, width=20)
rotateCounterButton.pack(side = TOP)

rotateClockwiseButton = Button(editingBox, text="Rotate Clockwise", command = rotateCounterFunction, width=20)
rotateClockwiseButton.pack(side = TOP)



img = ImageTk.PhotoImage(Image.open('image' + str(counter) + '.jpg'))
panel = Label(main, image=img)
panel.pack(side= LEFT, padx=20)


negativeButton = Button(editingBox, text="Negative Photo", command=negativeImageFunction, width=20)
negativeButton.pack(side = BOTTOM)

foilButton = Button(editingBox, text="Foil art", command=foilImageFunction, width=20)
foilButton.pack(side = BOTTOM)

pencilButton = Button(editingBox, text="Sharp Paint", command = paintImageFunction, width=20)
pencilButton.pack(side = BOTTOM)

oilButton = Button(editingBox, text="Oil Paint", command=oilImageFunction, width=20)
oilButton.pack(side = BOTTOM)

sketchButton = Button(editingBox, text="Sketch Light", command=sketchImageFunction, width=20)
sketchButton.pack(side = BOTTOM)

filterLabel = Label(editingBox, text = "Filters", font=16)
filterLabel.pack(side = BOTTOM, pady=10)

editingBox.pack()
main.mainloop()








