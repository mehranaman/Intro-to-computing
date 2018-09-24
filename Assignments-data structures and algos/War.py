#  File: War.py
#  Description: Card simulation
#  Student's Name: Naman Mehra
#  Student's UT EID: nm26465
#  Course Name: CS 313E 
#  Unique Number: 51470
#
#  Date Created: October 6th, 2017
#  Date Last Modified: October 6th, 2017



import random 
class Card:

    def __init__(self, Suit, Rank):
        self.Rank = Rank
        self.Suit = Suit

    def __str__(self):
        print(self.Rank + self.Suit)

class Deck:


    def __init__(self):
        Rank_list = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        Suit_list = ['C','D','H','S']
        self.cardList = []
        for suit in Suit_list:
            for rank in Rank_list:
                card = Card(suit, rank)
                self.cardList.append(card)

        
    def dealOne(self, object):
        object.hand.append(self.cardList[0])
        self.cardList = self.cardList[1:]
        
    def shuffle(self):
        random.shuffle(self.cardList)

    def __str__(self):
        for item in self.cardList:
            
            print(item, end = ' ')
        

class Player:
    hand = []
    handTotal = 0
    handNotEmpty = False
    
    def __str__(self):
        for i in self.hand:
            print(i)

def playGame(player1, player2):
    terminal_list = []
    Rank_list = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    dictRank = {}

    ranking = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    
    for ranking in ranking:
        dictRank[Rank_list[ranking-1]] = ranking
    round = 1
    while True:
            
        if player1.hand == []:
            print("Player 2 wins.")
            return
        if player2.hand == []:
            print("Player 1 wins.")
            return

        
        print("Player 1 has ", len(player1.hand), " card(s) in hand. They are:")
        for i in (player1.hand):
            print(i)

        print("Player 2 has ", len(player2.hand), " card(s) in hand. They are: ")
        for i in player2.hand:
            print(i)

            
        print("Round: ", round)
        print("Player 1 plays ", player1.hand[0], " face up.")
        print("Player 2 plays ", player2.hand[0], " face up")
    
        if dictR[player1.hand[0].Rank] > dictR[player2.hand[0].Rank]:
            print("Player 1 wins round ", round, ".")
            player1.hand.append (player2.hand[0])
            player1.handTotal += 1
            player2.hand = player2.hand[1:]
    

        elif dictR[player1.hand[0].Rank] > dictR[player2.hand[0].Rank]:
            print("Player 2 wins round ",round,".")
            player2.hand.append(player1.hand[0])
            player2.handTotal += 1
            player2.hand = player1.hand[1:]
            
        else:
            print("War starts: ", player1.hand[0], " = ", player2.hand[0])
            if len(player1.hand) < 4:
                print("Player 1 wins.")
                return
            elif len(player2.hand) < 4:
                print("Player 2 wins.")
                return
            else:
                while dictR[player1.hand[0].Rank] == dictR[player2.hand[0].Rank]:
                    if len(player1.hand) >= 4 and len(player2.hand) >= 4:
                        print("Player 1 plays ", player1.hand[1:4]," face down.")
                        print("Player 2 plays ", player2.hand[1:4], "face down.")
                        terminalList.append(player1.hand[0:4])
                        terminalList.append(player2.hand[0:4])
                        player1.hand = player1.hand[4:]
                        player2.hand = player2.hand[4:]
                    elif len(player1.hand) < 4:
                        print("Player 2 wins.")
                        return
                    else:
                        print("Player 1 wins.")
                        return
                

                if dictR[player1.hand[0].Rank] > dictR[player2.hand[0].Rank]:
                    print("Player 1 plays ", player1.hand, ".")
                    print("Player 1 wins round ",round, ".")
                    player1.hand.append(terminalList)
                    terminalList = []
                else:
                    print("Player 2 wins round ", round,".")
                    player2.hand.append(terminalList)
                    terminalList = []
                    
                    

        round += 1

            
                                  
def main():

    cardDeck = Deck()               # create a deck of 52 cards called "cardDeck"
    print("Initial deck:")
    print(cardDeck)                 # print the deck so we can see that you built it correctly
    
    random.seed(15)                 # leave this in for grading purposes
    cardDeck.shuffle()              # shuffle the deck
    print("Shuffled deck:")
    print(cardDeck)                 # print the deck so we can see that your shuffle worked
    
    player1 = Player()              # create a player
    player2 = Player()              # create another player

    for i in range(13):             # deal 26 cards to each player, one at 
       cardDeck.dealOne(player1)    #   a time, alternating between players
       cardDeck.dealOne(player1)
    
    playGame(player1,player2)

    
    print ("\n\nFinal hands:")    
    print ("Player 1:   ")
    print (player1)                 # printing a player object should print that player's hand
    print ("\nPlayer 2:")
    print (player2)                 # one of these players will have all of the cards, the other none
    
main()
                                  
                
                

            
                    
        
    

    

    
    




