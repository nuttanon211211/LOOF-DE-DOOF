# LOOF-DE-DOOF
A MTG like Card Game that use ML to resolve effects


### How to Play
Run game.py

### Functions
- This app support any card name and effects, as long as it is the okay format (see in decks) 
- This app support any effects but can resolve only three effects (healing, drawing, and damaging)

### Deck Format
- Decklist is the text file ended with .deck
- Each line of the in the file is in the card format

   Any line of text that does not have exactly three commas(",") is cosidered to be a note. So you can take a note like deck name and deck description


### The Card format
- [No. of Cards(number of copies)], Card_Name, Cost_of_card, Card_Effect
- Example :  2, PURRFECT CREATION, P1C1N1O1, DRAW 4
- No.of cards is the positive integer
- Card Name is anything that do not have commas (",")
- Cost of a Card is Upper-case P,C,N,O followed by a number(positive integer or zero) with nothing in between. The order of each cost elements do not matter
- Card Effect anything with effect number. The number must be Arabic numeral (1,2,3) but not the word (one,two,three). Multiple effects are seperated by a dot (".") (currently not tested)
 

### Valid cost example
    P1C1N1O1
    P1C1
    P1C1N0O0
    N3P1C2O4
    N10 O10 P5 C1
    O10-P5
    
### Valid card Effects
 - DRAW 2
 - HEAL 1
 - DAMAGE 4
 - draws 2 cards
 - heal you life by 5
 - Opponent takes 100 damages

### May not valid card Effects
- Draw two cards (Number is a word)
- draw 2 card but heals 3 damage (multiple effect not seperated by a dot(".") )
- heals 3 damage if you do draw 2 cards from the top of your deck (complicated)
- this card damage opponent by 1 damage, heals 3 damage from you,and if you do draw 2 cards from the top of your deck (complicated, not seperated by dots)
- ... (No effect texts)

### Get Creative with card Effects
- Hi I am Blissey, If you use me i will heal 3 damage from your and you will be healthier
- I am the pot of greed, When you play me I will draw 2 cards from top of your deck
- Zeraora V can do 160 damage to your opponent benched pokemon if certain codition is met

### Rules
- Player HP is the number of cards in the deck and in discarded combined
- Player with HP equal (or less than) zero lose the game
- When no card in the deck, player's discarded is shuffled and put back to the deck
- You can play anything as long as you can pay the cost
- You can pay the cost using Land cards
- You can play no more than one land per your turn
- (Don't worry about ruling too much, the game is run automatically)

### uwu
This app required tensorflow but not limited to
