import os
import sys
import time

letters = ["X", "O"]
lettersCounter = 0
won = False
ttt = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

winningpositions = [
	[0,1,2],
	[3,4,5],
	[6,7,8],
	[0,3,6],
	[1,4,7],
	[2,5,8],
	[0,4,8],
	[2,4,6]
]

template = f"""-------------
| {ttt[0][0]} | {ttt[0][1]} | {ttt[0][2]} |
|---|---|---|
| {ttt[1][0]} | {ttt[1][1]} | {ttt[1][2]} |
|---|---|---|
| {ttt[2][0]} | {ttt[2][1]} | {ttt[2][2]} |
-------------
"""


print(template)


def check():
		for indivwin in winningpositions:  # For each possible win take the index of 
			curriter = []
			for eachindex in indivwin:  # For each number in each possible run, append that index of the TTT table into a list.
				if eachindex in [0, 1, 2]:
					curriter.append(ttt[0][eachindex])
				if eachindex in [3, 4, 5]:
					curriter.append(ttt[1][eachindex - 3])
				if eachindex in [6, 7, 8]:
					curriter.append(ttt[2][eachindex - 6])
			if curriter == [letters[lettersCounter], letters[lettersCounter], letters[lettersCounter]]:
				return True
#				raise SystemExit

while won == False:

	askForPlacement = input(f"{letters[lettersCounter]}, where would you like to place your {letters[lettersCounter]}? ")

	if int(askForPlacement) in [1, 2, 3]:
		inde = 0
		sub = 1
	if int(askForPlacement) in [4, 5, 6]:
		inde = 1
		sub = 4
	if int(askForPlacement) in [7, 8, 9]:
		inde = 2
		sub = 7



	if ttt[inde][int(askForPlacement) - sub] in ["X", "Y"]:
		print("Spot has already been chosen! ")
		askForPlacement = input(f"{letters[lettersCounter]}, where would you like to place your {letters[lettersCounter]}? ")
	else:
		ttt[inde][int(askForPlacement) - sub] = letters[lettersCounter]
		os.system('clear')

	checkForWin = check()
	if checkForWin == True:
		won = True
		print(f"{letters[lettersCounter]}, you won!")
		time.sleep(1)

		askPlayAgain = input("Would you like to play again? ")
		os.system('clear')

		if askPlayAgain in ["Y", "y", "Yes", "Yes"]:
			lettersCounter = 0
			ttt = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
			template = f"""-------------
| {ttt[0][0]} | {ttt[0][1]} | {ttt[0][2]} |
|---|---|---|
| {ttt[1][0]} | {ttt[1][1]} | {ttt[1][2]} |
|---|---|---|
| {ttt[2][0]} | {ttt[2][1]} | {ttt[2][2]} |
-------------
"""
			won = False
		elif askPlayAgain in ["N", "n", "Yes", "yes"]:
			input("Press enter to close the game. ")
			sys.exit()


	template = f"""-------------
| {ttt[0][0]} | {ttt[0][1]} | {ttt[0][2]} |
|---|---|---|
| {ttt[1][0]} | {ttt[1][1]} | {ttt[1][2]} |
|---|---|---|
| {ttt[2][0]} | {ttt[2][1]} | {ttt[2][2]} |
-------------
"""

	if won == True:
		pass
	else:
		print(template)

	lettersCounter += 1
	lettersCounter %= 2