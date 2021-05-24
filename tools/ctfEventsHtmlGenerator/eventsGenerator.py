import os
import math

from bs4 import BeautifulSoup

filename = "awards.html"
inFile = os.path.join(os.path.abspath(os.path.dirname(__file__)), os.path.pardir, os.path.pardir, filename)

rootURL = "https://ctftime.org"

def getEventHtmlAsSoupObj():
	inputString = ""
	with open(inFile, "r") as f:
		inputString = f.read()

	htmlObj = BeautifulSoup(inputString, "html.parser")
	return htmlObj

def getInputTxtAsSoupObj():
	inputString = ""
	with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt"), "r") as f:
		inputString = f.read()

	htmlObj = BeautifulSoup(inputString, "html.parser")
	return htmlObj


if __name__ == "__main__":
	htmlObj = getInputTxtAsSoupObj()

	# events listed on ctftime
	currentEvents = [[_td.select_one("a") for _td in td.next_siblings][1] for td in htmlObj.select("[class='place_ico']")]

	""" Reset all to CSS class "button fit" """
	for i in range(0, len(currentEvents)):
		currentEvents[i]['href'] = rootURL + currentEvents[i]['href']
		currentEvents[i]['class'] = ["button", "fit"]

	""" Set 1,2 | 5,6 | 9,10 ... elements to CSS class "button primary fit" """
	for i in range(1, len(currentEvents), 4):
		currentEvents[i]['class'] = ["button", "primary", "fit"]
		if(i + 1) < len(currentEvents):
			currentEvents[i + 1]['class'] = ["button", "primary", "fit"]

	""" Create a new ul based on currentEvents """
	newUl = []
	for n in range(2):
		tmp = []
		for i in range(n, len(currentEvents), 2):
			tmp.append(currentEvents[i])
		newUl.append(tmp)

	""" Update the old ul to new ul """
	htmlObj = getEventHtmlAsSoupObj()
	oldUl = htmlObj.select("[class='actions stacked']")

	for n in range(len(oldUl)):
		# clear all elements under the ul
		oldUl[n].clear()
		for i in range(len(newUl[n])):

			# Update all li
			oldUl[n].insert(i, newUl[n][i].wrap(BeautifulSoup().new_tag("li")))

		print(oldUl[n])

	""" Finally write the updated html to a file """
	with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "awards.html"), "w") as f:
		f.write(htmlObj.prettify())

