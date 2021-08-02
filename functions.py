#Functions of LOOF DE DOOF game

#imports
import random
import re
from effectML import predictEffect



#Get the number of cards in the card pile
def numOfCards (deck):
    return len(deck)
  
#Calculate the cost of the card  
def cost (card):
    costP = re.findall(r"P(\d+)",card[1])
    costC = re.findall(r"C(\d+)",card[1])
    costN = re.findall(r"N(\d+)",card[1])
    costO = re.findall(r"O(\d+)",card[1])
    P,C,N,O = 0,0,0,0
    #print(costP,costC,costN,costO)
    if (len(costP) > 0):
        #print(costP[0])
        P = int(costP[0])
    
    if (len(costC) > 0):
        C = int(costC[0])
          
    if (len(costN) > 0):
        N = int(costN[0])
        #print(costN[0])
   
    if (len(costO) > 0):
        O = int(costO[0])
    return P,C,N,O
 
#Calculate the total cost of the card   
def totalCost (card):
    return sum(cost(card))
    
    
#Shuffle the deck
def shuffle(deck):
    if len(deck)<=1:
        return True
    for i in range(len(deck)-1, 0, -1):
        # Pick a random index from 0 to i
        j = random.randint(0, i + 1 -1)
        # Swap arr[i] with the element at random index
        deck[i], deck[j] = deck[j], deck[i]
    return True
    
#Reload the deck (put cards from the discarded into the deck)  
def reload(player):
    while player["Discarded"] != []:
        card = player["Discarded"].pop(0)
        player["Deck"].append(card)
        
    shuffle(player["Deck"])
    return True
        
 
#Create a player   
def createPlayer(name):
    player = dict()
    player["Deck"] = []
    player["Discarded"] = []
    player["Exiled"] = []
    player["Hand"] = []
    player["Land"] = []
    player["TappedLand"] = []
    player["name"] = name
    player["canPlayLand"] = True
    player["landCost"] = [0]*4
    
    return player
    
    
#Load the player's deck
def loadDeck(player,deck_path):
    file = open(deck_path, 'r')
    content = file.read()
    cardlist = content.split("\n")
    
    cardlist2 = []
    for e in cardlist:
        if len(e.split(",")) == 4:
            cardlist2.append([x.strip() for x in e.split(",")])
            
    cards = []
    for e in cardlist2:
        for i in range(int(e[0])):
            cards.append(e[1:])
    player["Deck"] = list(cards)
    return True
    
#Top card of play deck
def topCard(deck):
    return deck[0]

#################################### EFFECT ###############################


def discard(player):
    if player["Deck"] == [] and player["Discarded"] == []:
        return False
    if player["Deck"] == []:
        reload(player)
    card = player["Deck"].pop(0)
    player["Discarded"].append(card)
    return True

def discards(player,amount):
    for i in range(amount):
        discard(player)
       
       
        
def damage(player):
    if player["Deck"] == [] and player["Discarded"] == []:
        return False
    if player["Deck"] == []:
        reload(player)
    card = player["Deck"].pop(0)
    player["Exiled"].append(card)
    return True
    
def damages(player,amount):
    for i in range(amount):
        result = damage(player)
        if (result == False):
            return False
    return True  
      

# HEAL : Shuffle your Exiled face down, pick random cards(or top cards) of the counter that heals.
# Put it in your deck. Shuffle your deck
def heal(player):
    if player["Exiled"] == []:
        return False
    else:
        shuffle(player["Exiled"])
        card = player["Exiled"].pop(0)
        player["Deck"].append(card)
        shuffle(player["Deck"])
        return True
        
def heals(player,amount):
    for i in range(amount):
        result = heal(player)
        if (result == False):
            return False
    return True


def draw(player):
    if player["Deck"] == [] and player["Discarded"] == []:
        return False
    if player["Deck"] == []:
        reload(player)
    card = player["Deck"].pop(0)
    player["Hand"].append(card)
    return True

def draws(player,amount):
    for i in range(amount):
        result = draw(player)
        if (result == False):
            return False
    return True 
      


############################## END EFFECT ###############################



#If player lose
def lose2(player):
    if player["Deck"] == [] and player["Discarded"] == []:
        return True
    return False
  
#Current HP of a player  
def healthPoint(player):
    return len(player["Deck"]) + len(player["Discarded"])

#Check if the card is land card
def isLand(card):
    cardName = card[0]
    
    if cardName.upper().endswith("LAND"):
        return True
    else:
        return False
        
#Return the card description
def description(card):
    name = card[0]
    costP,costC,costN,costO = cost(card)
    effect = card[2]
    total_cost = totalCost(card)
    costdes = ""
    if (costP != 0):
        costdes += "["+str(costP)+"] Paws "
    if (costC != 0):
        if (costP != 0):
            costdes += "and "
        costdes += "["+str(costC)+"] Creativity "
    if (costN != 0):
        if (costP != 0 or costC !=0):
            costdes += "and "
        costdes += "["+str(costN)+ "] Nature "
    if isLand(card) == False:
        return name + " | costed [" + str(total_cost) + "] with at least "+costdes+" | effect: "+effect
    else:
        if costP == 0 and costC == 0 and costN == 0:
            return name + " | is given [" +str(costO) + "] Ordinary"
        return name + " | is given " +costdes 
    
    
    
#Print all card in the pile
def printCard(cards):
    num_card = len(cards)
    if num_card == 0:
        print("You have no card left.")
    else:
        for i in range(num_card):
            print("{"+str(i+1)+"}",description(cards[i]))
            
            
#Get the input number of cards
def playerCardSelector(cards):
    printCard(cards)
    if len(cards) == 0:
        return False
    value = input("Please enter a card number that you want to use:\n")
    while(value.isdigit()==False or int(value)<1 or int(value)>len(cards)):
        value = input("Please enter a card NUMBER that you want to use:\n")
    return int(value)
    

#Get the total cost of current active land
def totalLandCost(player):
    P,C,N,O = 0,0,0,0
    for card in player["Land"]:
        aP,aC,aN,aO = cost(card)
        P += aP
        C += aC
        N += aN
        O += aO
    return P,C,N,O
        
#Check if player can play a card
def canPlay(card,player):
    #costLand is #,#,#,#   P.C.N.O
    costLand = totalLandCost(player)
    if isLand(card):
        return player['canPlayLand']
    if totalCost(card) > sum(costLand):
        return False
    costCard = cost(card)
    for i in range(3):
        if costCard[i] > costLand[i]:
            return False
    return True
    
#Return character indicates ablity to play a card
def canPlayChar(card,player):
	if canPlay(card,player):
		return "O"
	else:
		return "X"


#Print cards in the hand
def printHand(player):
	cards = player['Hand']
	num_card = len(cards)
	if num_card == 0:
		print("You have no card left in your hand.")
	else:
		for i in range(num_card):
			print(canPlayChar(cards[i],player)+" {"+str(i+1)+"}",description(cards[i]))
	
#Select card in the hand	
def playerHandSelector(player):
	printHand(player)
	cards = player['Hand']
	if len(cards) == 0:
		return False
	value = input("Please enter a card number that you want to use:\n")
	while(value.isdigit()==False or int(value)<1 or int(value)>len(cards)):
		value = input("Please enter a card NUMBER that you want to use:\n")
	return int(value)	
	
    
    
#Check if player can play non-land card
def canplayNonLand(card,costArray):
    if totalCost(card) > sum(costArray):
        return False
    costCard = cost(card)
    costLand = costArray
    for i in range(3):
        if costCard[i] > costLand[i]:
            return False
    return True
    
    
#Tap a land
def tapLand(player,number):
    if number < 1:
        return False
    if number > numOfCards(player["Land"]):
        return False
    
    index = number-1
    card = player["Land"].pop(index)
    P,C,N,O = cost(card)
    player["TappedLand"].append(card)
    return P,C,N,O
    
    
#Handle when player pay the cost    
def payCost (card,player):
    player["landCost"] = [0]*4
    landCost = player["landCost"]
    while (canplayNonLand(card,landCost) == False):
        print("Cost of a card",cost(card))
        print("Current land cost",player["landCost"])
        print("Select the land to be tapped")
        number = playerCardSelector(player["Land"])
        tappedCost = tapLand(player,number)
        #Increase player["landCost"]
        for i in range(4):
            player["landCost"][i] += tappedCost[i]
    
    return True
    
#Handle when player play a card
def play(player,number,otherPlayer):
    if number < 1:
        return False
    if number > numOfCards(player["Hand"]):
        return False
    index = number-1
    if canPlay(player["Hand"][index],player) == False:
        return False
    card = player["Hand"].pop(index)
    
    if isLand(card):
        player["Land"].append(card)
    else:
        player["Discarded"].append(card)
        
    if isLand(card)==False:
        print("Pay the cost")
        payCost(card,player)
        resolveEffect(card,player,otherPlayer)
    else:
        player["canPlayLand"] = False
        
        
    return True

#Stand the land at the beginning of the turn
def standLand(player):
    while player["TappedLand"] != []:
        card = player["TappedLand"].pop(0)
        player["Land"].append(card)
        
    #shuffle(player["Deck"])
    return True
    
#Predict the number found, if not is 1 
def predictNumber(text):
    found = re.findall(r"(\d+)",text)
    if len(found)==0:
        return 1
    else:
        return int(found[0])
        
        
#Resolves the effect
#import : from effectML import predictEffect
def resolveEffect(card,player,otherPlayer):
    effects = card[2].split('.')
    #print(effects)
    for e in effects:
        effectFunction = predictEffect(e)
        effectNumber = predictNumber(e)
        #print(effectFunction,"..",effectNumber)
        if effectFunction == "DRAW":
            draws(player,effectNumber)
        elif effectFunction == "HEAL":
            heals(player,effectNumber)
        elif effectFunction == "DAMAGE":
            damages(otherPlayer,effectNumber)
        
    return True
    
    
#Handle  and check if player lose
def loseHandler(player):
    if lose2(player):
        print(player["name"],' lose')
        return True
    return False
    
    
#Display and Handle other options of the game
def otherFunction(player):
    functions = ["Check Land","Check Status","Concede"]
    
    for i in range(len(functions)):
        print("{"+str(i+1)+"} :",functions[i])
    value = input("Please enter the number that you want to use:\n")
    while(value.isdigit()==False or int(value)<1 or int(value)>len(functions)):
        value = input("Please enter the NUMBER that you want to use:\n")
    
    value = int(value)
    if value == 1:
        printCard(player["Land"])
        print()
        
    if value == 2:
        numOfCards(player["Land"])
        print("You have",numOfCards(player["Deck"]),"cards in your deck.")
        print("You have",numOfCards(player["Discarded"]),"cards in your discarded.")
        print("You have",numOfCards(player["Exiled"]),"cards in your exiled.")
        print("You have",numOfCards(player["Hand"]),"cards in your hand.")
        print("You have",numOfCards(player["Land"]),"cards in your land.")
        print("You have",numOfCards(player["TappedLand"]),"cards in your tapped land.")
        print("Your name is",player["name"])
        print()
    
    if value == 3:
        value = input("Press C to concede:\n")
        if value.strip().upper() == "C":
            damages(player,100)
            

            
#Handle the turn of a player
def turn(player,otherPlayer):
    if loseHandler(player): return True
    print("Draw a card")
    draw(player)
    print("Stand the Land")
    standLand(player)
    player["canPlayLand"] = True
    
    command = ["E","O"]
    #value = input("P:play card E:end turn:\n")
    if loseHandler(player): return True
    while(True):
        if loseHandler(player): return True
        
        print("Your HP",healthPoint(player)," : ","Opponent HP",healthPoint(otherPlayer))
        printHand(player)
        value = input("[Number]:play card E:end turn O:other :\n")
        while ((value.strip().upper() not in command) and \
               (value.strip().isdigit() == False or int(value)<1 or int(value)>len(player["Hand"]) ) ):
            value = input("[NUMBER]:play card E:end turn O:other :\n")
            
        if value.strip().isdigit():
            print("Play a card")
            #number = playerCardSelector(Player["Hand"])
            number = int(value)
            res = play(player,number,otherPlayer)
            if res == False:
                print("Cannot be played")
            
        if value.strip().upper() == "E":
            player["canPlayLand"] = True
            print("Turn Endo")
            print()
            return True
        
        if value.strip().upper() == "O":
            otherFunction(player)
        
    
#Reset the player's deck and restart
def restart(player):
    while player["Discarded"] != []:
        card = player["Discarded"].pop(0)
        player["Deck"].append(card)
        
    while player["Exiled"] != []:
        card = player["Exiled"].pop(0)
        player["Deck"].append(card)  
    
    while player["Hand"] != []:
        card = player["Hand"].pop(0)
        player["Deck"].append(card) 
        
    while player["Land"] != []:
        card = player["Land"].pop(0)
        player["Deck"].append(card)
    
        
    shuffle(player["Deck"])
    player["canPlayLand"] = True
    player["landCost"] = [0]*4
    return True
        
#The GAME handler   
def game(player1,player2):
    print("Ready")
    restart(player1)
    restart(player2)
    
    players = [player1,player2]
    
    counter = 0
    
    while(True):
        print("Turn",counter+1)
        print(players[counter%2]["name"],"turn")
        turn(players[counter%2], players[(counter+1)%2])
        counter += 1
        lose1 = loseHandler(players[0])
        lose2 = loseHandler(players[1])
        if lose1 or lose2:
            print("Game Over")
            return True
        

        
        
