from graphics import *
import random
def main():
	widthLimits = [200, 500]
	heightLimits = [300, 600]
	width = input("Enter width: ")
	while width.isalpha():
		print("Width must be number")
		width = input("Enter width: ")
		print(width)
	width = float(width)
	print(width)
	while not widthLimits[0] < width < widthLimits[1]:
		print("Width must be between %d and %d" % (widthLimits[0], widthLimits[1]))
		width = input("Enter width: ")
		print(width)
		while width.isalpha():
			print("Width must be a number")
			width = input("Enter width")
			print(width)
		width = float(width)
		print(width)
	height = float(input("Enter height: "))
	print(height)
	while not heightLimits[0] < height < heightLimits[1]:
		print("Height must be between %d and %d" % (heightLimits[0], heightLimits[1]))
		width = float(input("Enter height: "))
		print(width)
	win = GraphWin("Fortnite is lit", width, height)
	win.setCoords(0, 0, width, height)
	rect = Rectangle(Point(0, height/7), Point(height*1/7, 0))
	rect.draw(win)
	win.getMouse()
	win.close()
main()