#Jeffrey Almanzar


from random import *
 
class Blackjack:
    '''This is the top level class that controls the whole game.'''
 
    def __init__(self):
        self.UI = UserInterface()#creates an object UserInterface, which inherits info from the classes: Deck and Hand.
        self.hand = 1 #number of rounds played
         
         
     
    def startgame(self):
        '''Starts the game.'''
        self.UI.printIntro()#print an introduction to the game
        self.playround()    #play a complete round
        self.score = self.UI.getscore()#gets the score of the round played
         
        while self.continuegame() and self.UI.check():
             
            self.playround()
            self.hand = self.hand + 1 #Updates the number of hand played
            self.score = self.score + self.UI.getscore() #Accomulates the score the player is getting each round
        if self.UI.check() == False: #checks if the deck is empty and lets the user know why the game stopped
            print("The game is over because the deck is empty.")
        self.finalscore()
             
    def playround(self):
        '''play one round of the game.'''
         
        self.UI.mixCards()#Mixes the cards
        self.UI.Deal()    #gives to cards to te player and removes them from the deck
        self.UI.showCards() #show the user the cards he has
        if self.UI.check == False:
            self.UI.printResults()
        else:
            self.UI.addcard() #asks the user if he wants to add another card
            self.UI.printResults()
             
 
    def continuegame(self):

            '''Asks the user if he wants to play another round.'''
            user = input("Would you like to play another round? yes or no --> ").lower()
            if user[0]== 'y':
                print()
                self.UI.cardsinDeck()
                self.UI.erasecard()
                 
                return True
             
            else:
                return False
         
    def finalscore(self):
        ''' Calculates the score the user receives and returns it '''
        score = round(self.score /self.hand,2)
        print()
        print("...................................................")
        print(".....................GAME OVER!....................")
        print("...................................................")
        print("RESULTS")
        print("...................................................")
        print("You played",self.hand,"rounds")
        print("Your culmulative score was",self.score)
        print("Your final score is --> ",score)
        print("Thanks for playing")
 
 
class Deck:
    '''This class builds and keeps track of the cards in the deck.'''
    def __init__(self):
        '''Builds the deck that is going to be used to play/
        via a list of tupples. The list is then shuffled'''
         
        self.deck = []
        self.userCards = []
        for i in ("hearts","spades","clubs","diamonds"):
            for j in  range (1,14):
                self.deck.append(((j,i)))
                 
    def mixCards(self):
        #This method will shuffle the cards
        return shuffle(self.deck)
     
 
    def Deal(self):
        ''' Will remove top card in deck and give it to the player'''
        if len(self.deck)<=2:
            self.userCards.append(self.deck[0])
            self.deck.remove(self.deck[0])
            self.userCards.append(self.deck[0])
            self.deck.remove(self.deck[0])
            return self.deck
        else:
            self.userCards.append(self.deck[0])
            self.userCards.append(self.deck[1])
            self.deck.remove(self.deck[0])
            self.deck.remove(self.deck[1])
            return self.deck #return the cards left in the deck
 
    def check(self):
        ''' Method will check if there are cards left in the deck/
        will stop game if deck is empty'''
        if len(self.deck) >= 1:
            return True
        else:
            return False
         
 
class Hand(Deck):
    '''Takes care of the player' cards.'''
    def __init__(self):
        Deck.__init__(self) 
     
    def Showhand(self):
        ''' Returns the cards the user has'''
        return self.userCards
     
    def addcard(self):
        ''' adds the card dealt from the deck to the player'''
        pass #not used right now
             
         
 
class UserInterface(Hand):
    '''This class show information to the user.'''
    def __init__(self):
        Hand.__init__(self)
        self.score = 0
 
     
    def printIntro(self):
        '''Prints out introduction and rules to the player'''
        print("This is the Blackjack game.")
        print("read online for rules.")
        print("...........................")
        print("Let's start")
        print("...........................")
 
     
    def showCards(self):
        '''displays the cards in the players hands.'''
        print("These are your cards:"+"\n",self.userCards)
        self.handnumber = 2
        cardsum = 0
        for i in range(0,len(self.userCards)):
            cardsum =cardsum + self.userCards[i][0]
        print("Your current card sum is:", cardsum)

    def cardsinDeck(self):
        '''This method tells the user how many cards are in the deck.'''
        print("There are",len(self.deck),"cards left in the deck.")
        return len(self.deck)
         
    def Hit(self):
        '''asks the user whether the want to be dealt
        another card or continue the game.'''
        if self.check == False:
            return False
        else:
            user = input("Would you like to add another card? yes or no --> ").lower()
            if user[0]== 'y':
                return True
            else:
                return False
             
         
    def addcard(self):#addcard method from the class Hand overriden
        while self.Hit():
            if len(self.deck)>0:    
                self.userCards.append(self.deck[0])
                self.deck.remove(self.deck[0])
                self.showCards()
            else:
                break
    def erasecard(self):
        self.userCards.clear()
         
     
    def printResults(self):
        '''This method prints the score of the player.'''
         
        sumcards = 0
        for i in self.userCards:
            sumcards = sumcards + i[0]
             
        if sumcards >= 12 and sumcards <=21:
            self.score = sumcards
        else:
            self.score = 0
             
        print("The sum of your card is --> ",sumcards)
        print("Thefore, your score is --> ",self.score)
        print("...................................................")
        print("ROUND ENDED!")
        print("...................................................")
 
    def getscore(self):
        '''This method gets the score of each round'''
        return self.score
     
 
#Testing the game
def main():
    g = Blackjack()
    g.startgame()
main()
