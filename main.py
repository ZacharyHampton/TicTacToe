import os
import sys
import time

letters = ["X", "O"]
lettersCounter = 0
won = False
ttt = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]  # Game table

winningpositions = [  # All winning positions in TicTacToe
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
"""  # Game table template, makes the game look nice.


print(template)

def checkForDupe(input):  # Function checks if letter is already in slot
	if input in letters:
		return True
	else:
		return False


def checkForError(input):  # Function checks for out of range numbers, and non-int numbers.
	try:
		if int(input) < 1 or int(input) > 9:
			return "OOR"
	except (ValueError, TypeError):
		return "NINT"

	else:
		return "OK"


def check(): # function will loop through each indice of the possible winning combinations, and compare them to my game table. If one of the winning combinations has 3 of the same letter in the list, then it is classified as a win. If any of the indices in an array are not its respectable 3 numbers, iterate a counter. If all the spots are taken, they are not numbers, and will be different, therefore ticking our counter. Since the table is 9 slots, once the counter is equal to 9, the round is a tie. 
		tttc = 0
		for (a, b, c) in zip(ttt[0], ttt[1], ttt[2]):
			if a not in ["1", "2", "3"]:
				tttc += 1
			if b not in ["4", "5", "6"]:
				tttc += 1
			if c not in ["7", "8", "9"]:
				tttc += 1

		if tttc == 9:
			return "Tie"

		for indivwin in winningpositions:  # For each possible win take the index of 
			curriter = []
			for eachindex in indivwin:  # For each number in each possible run, append that index of the TTT table into a list.
				if eachindex in [0, 1, 2]:
					curriter.append(ttt[0][eachindex])
				if eachindex in [3, 4, 5]:
					curriter.append(ttt[1][eachindex - 3])
				if eachindex in [6, 7, 8]:
					curriter.append(ttt[2][eachindex - 6])
			if curriter == [letters[lettersCounter], letters[lettersCounter], letters[lettersCounter]]:  # If current win combination has all of your letters, you win.
				return True

while won != True:  # Loop inf if you have not won.

	askForPlacement = input(f"{letters[lettersCounter]}, where would you like to place your {letters[lettersCounter]}? ")

	checkForErrorReturn = checkForError(askForPlacement)  # Check for out of range/not-int nums to prevent errors.
	if checkForErrorReturn == "OOR":  # If out of range.
		while True:
			print("Your number is out of range. Please choose a number from 1 to 9.")
			askForPlacement = input(f"{letters[lettersCounter]}, where would you like to place your {letters[lettersCounter]}? ")
			checkForErrorReturn = checkForError(askForPlacement)
			if checkForErrorReturn == "OK":
				break
	if checkForErrorReturn == "NINT": # If not-integer.
		while True:
			print("Your number is not an integer. Please try again.")
			askForPlacement = input(f"{letters[lettersCounter]}, where would you like to place your {letters[lettersCounter]}? ")
			checkForErrorReturn = checkForError(askForPlacement)
			if checkForErrorReturn == "OK":
				break
		

	if int(askForPlacement) in [1, 2, 3]: # Get number to subtract, and curr indice for nested table.
		inde = 0
		sub = 1
	if int(askForPlacement) in [4, 5, 6]:
		inde = 1
		sub = 4
	if int(askForPlacement) in [7, 8, 9]:
		inde = 2
		sub = 7

	isDupe = checkForDupe(ttt[inde][int(askForPlacement) - sub])

	if isDupe == True: # If spot has letter in it:
		while True:
			print("Spot has already been chosen! ")
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
			isDupe = checkForDupe(ttt[inde][int(askForPlacement) - sub])
			if isDupe == False:
				break
	if isDupe == False:
		ttt[inde][int(askForPlacement) - sub] = letters[lettersCounter] # Sets player's letter in chosen position
		os.system('clear')


	checkForWin = check()  # Check for tie or win


	if checkForWin == True or checkForWin == "Tie": # If win or tie, stop loop.
		won = True
		if checkForWin == True:
			print(f"{letters[lettersCounter]}, you won!")
		if checkForWin == "Tie":
			print("The game is a tie!")
		time.sleep(1)

		askPlayAgain = input("Would you like to play again? ")
		os.system('clear')

		if askPlayAgain in ["Y", "y", "Yes", "Yes"]:
			lettersCounter = 0
			ttt = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]  # Set table to normal.
			template = f"""-------------
| {ttt[0][0]} | {ttt[0][1]} | {ttt[0][2]} |
|---|---|---|
| {ttt[1][0]} | {ttt[1][1]} | {ttt[1][2]} |
|---|---|---|
| {ttt[2][0]} | {ttt[2][1]} | {ttt[2][2]} |
-------------
"""  # Reassign variables in fancy table.
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
"""  # Reassign variables to fancy table.

	if won == True:
		pass
	else:
		print(template)

	lettersCounter += 1  # Both of these lines needed to switch letters each loop/round.
	lettersCounter %= 2