
from random import *
class GameControl:
    '''This is the top level class that control the game,
        using the classes: UserInterface, Cards, and PlayGame.'''

    def __init__(self):
        '''Construts two objects of type UserInterface and Statistics.'''
        self.UI = UserInterface()
        self.stats = Statististics()

        
    def startPlaying(self):
        '''This method will start and control the entire game.'''
        self.UI.printIntro()#Prints an introduction to the game
        self.playRound()#Play one round of the game
        while self.UI.continueplay():#Determines if the game should be continued
            self.playRound()#Play a complete round again
        self.stats.printFinalresult()#prints the final results
            
        
    def playRound(self):
        '''This method play a round of the game.'''
            
        self.stats.mixCards()
        self.stats.giveCards()
        self.stats.showLosercard()
        user = self.UI.keep_or_switch()
        self.stats.changeCard(user)
        self.stats.printResult()
        print('.....................................................')
        

class UserInterface:
    '''This is the class that prints out information to the player.'''

    def printIntro(self):
        '''This method prints an introduction to the game.
            It states the rules of the game.'''
        print('.....................................................')
        print("              Stay or Switch Game                    ")
        print('.....................................................')
        print("If you do not know how to play, see the rules online.")
        print('.....................................................')
    def keep_or_switch(self):
        '''This method asks the user if he wants to
            keep the card selected or if he wants to switch it.
            It returns True, if he wants to keep it.
            Otherwise, it returns False.'''
        player = input("Would you like to keep or switch your card? type: k or s ---> ").lower()
        if player[0] == 's':
            return True
        else:
            return False
    
    def continueplay(self):
        '''This method asks the player if he wants to play again.
            Return true if he wants to. Otherwise, returns false.'''
        user = input('Would you like to play another round? y or n ---> ').lower()
        if user[0] == 'y':
            return True
        else:
            return False
            

class Cards:
    '''This is the class that keeps track of the cards.'''

    def __init__(self):
        '''constructs the cards'''
        self.labels = ['WINNER','LOSER',"LOSER"]
        
    def mixCards(self):
        '''This returns the cards mixed as a list.'''
        shuffle(self.labels)
        return self.labels
    
    def giveCards(self):
        '''This method gives the choice to the pleyer to select one card'''
        self.player = int(input("Choose a card from the table:\n   1   2   3 ---> "))
        print("You have selected card",self.player)
        self.player = self.player - 1


    
    def showLosercard(self):
        '''This method show one of the two loser cards to the player.'''
        #player_card = self.getCard()#Current player's card
        for i in range(3):
            if self.labels[i] == "LOSER" and i != self.player:
                if i == 0:
                    print("  LOSER  2   3")
                    self.current = [1,2]#current cards facing down
                    break
                elif i == 1:
                    print("  1  LOSER   3")
                    self.current = [0,2]#current cards facing down
                    break
                else:
                    print("  1  2  LOSER")
                    self.current = [0,1]#current cards facing down
        print("Chances of wining increased!")
                    
    def changeCard(self,boolean):
        '''Will change and ruturn the current card the player has'''
        self.boolean = boolean
        if self.boolean == True:
            if self.current[0] != self.player:
                self.player = self.current[0]
            elif self.current[1] != self.player:
                self.player = self.current[1]
                
        else:
            pass
        return self.player
                         

class Statististics(Cards):
    '''This class  keeps  track of the number of wins and losses. And also display this information'''

    def __init__(self):
        Cards.__init__(self) #Gets info from the Cards class
        self.win = 0 #Keeps track of the number on winnings
        self.losses = 0 #Keeps track of the number on winnings
        
    def printResult(self):
        '''This method tell the user if he wins or loses a round'''
        if self.labels[self.player] == "WINNER":
            self.win = self.win + 1
            print('You Won!! card',self.player + 1,'was the winning one.')
            print(self.labels)
        else:
            self.losses = self.losses + 1
            print('You Lost!! card',self.player + 1,'was not the winning one.')
            print(self.labels)
            
        

    def printFinalresult(self):
        '''Prints the final results'''
        print('.....................................................')
        print("                       Game Over                     ")
        print('.....................................................')
        print("RESULTS")
        print('.....................................................')
        print('You played --->',self.win + self.losses,'rounds.')
        print('You won    --->',self.win,'times.')
        print('You lost   --->',self.losses,'times.')

#TESTING
def main():
    A = GameControl()
    A.startPlaying()
main()
