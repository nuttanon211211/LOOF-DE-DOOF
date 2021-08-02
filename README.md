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

### The Card format
- [No. of Cards], Card_Name, Cost_of_card, Card_Effect
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
- this card damage opponent by 1 damage, heals 3 damage from you,and if you do draw 2 cards from the top of your deck


### owo
This app required tensorflow but not limited to
