from functions import *
import os


def startScreen():
	print("LOOF DE DOOF")
	print()
	print()
	print("press enter")
	return True
	
def enterHandler():
	inputs = input()
	return inputs
	
def decksWarning():
	if 'decks' not in os.listdir():
		print("Not have a folder 'decks' in a directory")
		print("You may encounter a bug")
	return True
	
def numberOfDecks(directory):
    count = 0
    for e in os.listdir(directory):
        if e.endswith(".deck"):
            count +=1
            
    return count
    
    
def showDecks():
	print("avaliable decks :  ")
	for e in os.listdir("decks"):
		if e.endswith(".deck"):
			print(e.strip(".deck"))

def playerNameInput():
	name1 = input("Enter name for player 1: ")
	name2 = input("Enter name for player 2: ")
	name1 = name1.strip()
	name2 = name2.strip()
	if name1 == "":
		name1 = "P1"
	if name2 == "":
		name2 = "P2"
	return name1 , name2
	
def loadDeckHandler(player1,player2):
	deckDict = dict()
	count = 1
	for e in os.listdir("decks"):
		if e.endswith(".deck"):
			deckDict[count] = e.strip(".deck")
			count += 1
			
			
	print("avaliable decks :  ")
	for k,v in deckDict.items():
		print('{'+str(k)+"}",v)
		
	value1 = input("Choose the deck for player 1 (enter number): ")
	while value1.isdigit() == False or int(value1) not in deckDict.keys():
		value1 = input("(Deck not exist) Re-Choose the deck for player 1 (enter number): ")
	
	value2 = input("Choose the deck for player 2 (enter number): ")
	while value2.isdigit() == False or int(value2) not in deckDict.keys():
		value2 = input("(Deck not exist) Re-Choose the deck for player 2 (enter number): ")
		
	loadDeck(player1,"decks/"+deckDict[int(value1)]+".deck")
	loadDeck(player2,"decks/"+deckDict[int(value2)]+".deck")
	
	return True
	
	
startScreen()
decksWarning()
enterHandler()
if numberOfDecks('decks') == 0:
	print("No deck in the 'decks', Plaese add more decks")
	enterHandler()
	exit(0)

name1 , name2 = playerNameInput()
P1 = createPlayer(name1)
P2 = createPlayer(name2)

loadDeckHandler(P1,P2)

playAgain = True
while (playAgain):
	game(P1,P2)
	value = input("Play Again (Y , N)")
	while value.strip().upper() not in ["Y","N"]:
		value = input("Play Again (Y , N)")
	if  value.strip().upper() == "N":
		playAgain = False
		
	
