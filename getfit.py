from graphics import *
def getDays(dataFile):
	days = []
	file = open(dataFile, "r")
	for index in range(len(file.readlines())):
		file.close()
		file = open(dataFile, "r")
		days.append(file.readlines()[index][:3])
		#appends the first three letters of the day
	return days
def getData(dataFile):
	data = []
	file = open(dataFile, "r")
	for index in range(len(file.readlines())):
	#for index in range(number of days)
		file.close()
		file = open(dataFile, "r")
		for i in range(len(file.readlines()[index])):
		#for i in range(len(line number index))
		#first the first line, then second, etc.
			file.close()
			file = open(dataFile, "r")
			if file.readlines()[index][i] == " ":
			#if the first character, then second, etc.
				file.close()
				file = open(dataFile, "r")
				data.append(int(file.readlines()[index][i:]))
				#appends from the " " to the end, or the number of steps the person walked and turns it from a string to an integer
	return data
def checkValidNum(var, limits):
	if not var.isalpha():
	#if var is a string of numbers or symbols:
		if not var.isnumeric():
		#if var includes a symbol:
			for i in range(len(var)):
				if var[i] == ".":
					floatNums = []
					#list of the two numbers before and after the "." 
					floatNums.append(var[:i])
					floatNums.append(var[i:])
					break
			else:
				return False
			if not floatNums[0].isnumeric() and not floatNums[1].isnumeric():
			#if both of the numbers in the list floatNums are not numbers:
				return False
		var = float(var)
		if limits[0] < var < limits[1]:
			return True
	return False
	#if var is a letter: return False
def checkAlpha(var):
	for char in var:
		if char.isalpha():
			return False
	return True
def main():
	goalLimits = [1000, 20000]
	widthLimits = [200, 2500]
	heightLimits = [200, 1300]
	dataFile = input("Enter filename with step data: ")
	goal = input("Enter step goal: ")
	while not checkValidNum(goal, goalLimits):
		while not checkAlpha(goal):
			print("Invalid entry: Must be numeric")
			goal = input("Enter step goal: ")
		print("Invalid entry: Must be between %d and %d" % (goalLimits[0], goalLimits[1]))
		goal = input("Enter step goal: ")
	goal = float(goal)
	width = input("Enter width of the window: ")
	while not checkValidNum(width, widthLimits):
		while not checkAlpha(width):
			print("Invalid entry: Must be numeric")
			width = input("Enter width of the window: ")
		print("Invalid entry: Must be between %d and %d" % (widthLimits[0], widthLimits[1]))
		width = input("Enter width of the window: ")
	width = float(width)
	height = input("Enter height of the window: ")
	while not checkValidNum(height, heightLimits):
		while not checkAlpha(height):
			print("Invalid entry: Must be numeric")
			height = input("Enter height of window: ")
		print("Invalid entry: Must be between %d and %d" % (heightLimits[0], heightLimits[1]))
		height = input("Enter height of the window: ")
	height = float(height)
	bottomHeight = height*7/8
	days = getDays(dataFile)
	data = getData(dataFile)
	averageSteps = 0
	totalSteps = 0
	for num in data:
		averageSteps += num
		totalSteps += num
	averageSteps = averageSteps/len(data)
	win = GraphWin("Get Fit", width, height)
	win.setCoords(0, 0, width, height)
	win.setBackground("light gray")
	top = Rectangle(Point(0, height), Point(width, bottomHeight))
	top.draw(win)
	top.setFill("white")
	goalText = Text(Point(width*4/32, (height+bottomHeight)/2), "Daily goal: %.0f" % (goal))
	averageText = Text(Point(width*15/32, (height+bottomHeight)/2), "Average steps: %d" % (averageSteps))
	totalText = Text(Point(width*26/32, (height+bottomHeight)/2), "Total steps: %d" % (totalSteps))
	day1Text = Text(Point(width/14, height/20), days[0])
	day2Text = Text(Point(width*3/14, height/20), days[1])
	day3Text = Text(Point(width*5/14, height/20), days[2])
	day4Text = Text(Point(width*7/14, height/20), days[3])
	day5Text = Text(Point(width*9/14, height/20), days[4])
	day6Text = Text(Point(width*11/14, height/20), days[5])
	day7Text = Text(Point(width*13/14, height/20), days[6])
	texts = [goalText, averageText, totalText, day1Text, day2Text, day3Text, day4Text, day5Text, day6Text, day7Text]
	biggestNum = max(data)
	baseLine = bottomHeight/biggestNum
	bars = []
	bar1 = Rectangle(Point(0, baseLine*data[0]), Point(width/7, 0))
	bar2 = Rectangle(Point(width/7, baseLine*data[1]), Point(width*2/7, 0))
	bar3 = Rectangle(Point(width*2/7, baseLine*data[2]), Point(width*3/7, 0))
	bar4 = Rectangle(Point(width*3/7, baseLine*data[3]), Point(width*4/7, 0))
	bar5 = Rectangle(Point(width*4/7, baseLine*data[4]), Point(width*5/7, 0))
	bar6 = Rectangle(Point(width*5/7, baseLine*data[5]), Point(width*6/7, 0))
	bar7 = Rectangle(Point(width*6/7, baseLine*data[6]), Point(width, 0))
	goalBar = Line(Point(0, baseLine*goal), Point(width, baseLine*goal))
	bars = [bar1, bar2, bar3, bar4, bar5, bar6, bar7]
	goalBar.draw(win)
	for index in range(len(bars)):
		bars[index].draw(win)
		if bars[index].getP1().getY() < goalBar.getP1().getY():
			bars[index].setFill("red")
		else:
			bars[index].setFill("green")
	for index in range(len(texts)):
		texts[index].draw(win)
		if width < 1221:
			texts[index].setSize(int(width/40))
		else:
			texts[index].setSize(int(width/70))
	win.getMouse()
	win.close()
main()