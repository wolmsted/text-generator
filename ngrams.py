# This program takes in a text file and creates random text snippets in the style
# of the given file. See readme for more information.															

import sys
import random

MIN_NVALUE = 2

# asks the user for the N-value and checks for malformed inputs
def getNValue():
	nvalue = raw_input("Value of N? ")
	while (not nvalue.isdigit() or int(nvalue) < MIN_NVALUE):
		print("Invalid input. Please enter integer value greater than or equal to %d" % (MIN_NVALUE))
		nvalue = raw_input("Value of N? ")
	return int(nvalue)

# reads in the file to a list
def readFile(fileName):
	try:
		txtFile = open(fileName)
		wordList = []
		for line in txtFile:
			for word in line.split():
				wordList.append(word)
		txtFile.close()
		return wordList		
	except IOError:
		print("ERROR: File '%s' not found. " % (fileName))
		quit()

# creates a dictionary from the list and given nvalue
def createDict(nvalue, wordList):
	dictionary = {}
	for index, val in enumerate(wordList):
		tupleKey = ()
		valueList = []
		ncount = 0
		while ncount < nvalue - 1:
			if (index + ncount >= len(wordList)):
				tupleKey += (wordList[index + ncount - len(wordList)],) # string converted to tuple
			else:
				tupleKey += (wordList[index + ncount],)
			ncount += 1
		if dictionary.has_key(tupleKey):
			valueList = dictionary.get(tupleKey)
		if (index + nvalue - 1 >= len(wordList)):
			valueList.append(wordList[index + nvalue - 1 - len(wordList)])
		else:
			valueList.append(wordList[index + nvalue - 1])
		dictionary[tupleKey] = valueList
	return dictionary

# goes through the dictionary and prints the words required
def displayText(nvalue, wordCount, dictionary):
	currKey = random.choice(dictionary.keys())
	ncount = 0
	while (ncount <= wordCount - (nvalue - 1)):
		if ncount == 0:
			string = ' '.join(map(str, currKey))
			print "... " + string,
		else:
			value = dictionary[currKey]
			tupleAsList = list(currKey) # sets tuple to list so it can be edited
			del tupleAsList[0]
			if len(value) > 1:
				tupleAsList.append(value[random.randint(0, len(value) - 1)])
			else:
				tupleAsList.append(value[0])
			print tupleAsList[len(tupleAsList) - 1],
			currKey = tuple(tupleAsList)
		ncount += 1
	print(" ...")

# repeats the process until the user wants to quit
def repeat(nvalue, dictionary):
	while True:
		print("")
		wordCount = raw_input("Number of random words to generate (0 to quit)? ")
		while (not wordCount.isdigit() or int(wordCount) < nvalue and int(wordCount) != 0):
			print("Invalid input. Please enter integer value greater than your N-value. ")
			print("")
			wordCount = raw_input("Number of random words to generate (0 to quit)? ")
		if (int(wordCount) == 0):
			return
		else:
			displayText(nvalue, int(wordCount), dictionary)

# main function handles incorrect arguments
def main():
	print("")
	print("Welcome to the text-generator. Given a text file as an argument, this program will")
	print("create a snippet of text that follows the same style of the given file. You will provide")
	print("an N-Value which determines the level of randomness in the words, the lower the more random")
	print("the higher the more similar to the originial file.")
	print("")
	argLen = len(sys.argv)
	if argLen < 2:
		print("ERROR: No file given.")
	else:
		if argLen > 2:
			print("Ignoring excess arguments... ")
		nvalue = getNValue()
		dictionary = createDict(nvalue, readFile(sys.argv[1]))
		repeat(nvalue, dictionary)


if __name__ == "__main__":
    main()
