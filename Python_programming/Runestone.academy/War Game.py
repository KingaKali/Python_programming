# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 19:49:49 2021

@author: Kinga Kalinowska
"""
import random

class Card:
    def __init__(self,CardSuit,CardValue):
        self.Card_suit=CardSuit
        self.Card_value=CardValue
        
    def show(self):
        print("{} of {}".format(self.Card_value,self.Card_suit))
        
    def get_card_value(self):
        return self.Card_value
    
    def get_card_suit(self):
        return self.Card_suit

class CardDeck(Card):
    def __init__(self):
        #Card.__init__(self)
        self.cards=[]
        self.build()
        self.shuffle()
        
        
    def build(self):
        
        for s in ["Spades","Clubs","Diamonds","Hearts"]:
            for v in [ '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13','14']:
                      self.cards.append(Card(s,v))
    
    def show(self):
        for c in self.cards:
            c.show()
            
    def shuffle(self):
        random.shuffle(self.cards)
        
    def get_cards(self):
        return self.cards

class War_Game(CardDeck):
    def __init__(self):
        CardDeck.__init__(self)
        cards=self.get_cards()
        number_of_cards=int(len(cards)/2)
        self.a_cards=cards[:number_of_cards]
        self.b_cards=cards[number_of_cards:]
    
    def play_war_game(self):
        round=1
        while self.a_cards and self.b_cards: 
            a_card=self.a_cards.pop()
            b_card=self.b_cards.pop()
            card_on_stash=[]

            
            while a_card.get_card_value()==b_card.get_card_value():
                if len(self.a_cards)>=2 and len(self.b_cards)>=2:
                    card_on_stash= card_on_stash + [a_card,b_card,self.a_cards.pop(),self.b_cards.pop()]
                    a_card = self.a_cards.pop()
                    b_card=self.b_cards.pop()
        
                elif len(self.b_cards)==0:
                    card_on_stash= card_on_stash + [a_card,b_card,self.a_cards.pop(),self.a_cards.pop()]
                    a_card = self.a_cards.pop()
                    b_card=self.a_cards.pop()
                    
                elif len(self.a_cards)==0:
                    card_on_stash= card_on_stash + [a_card,b_card,self.b_cards.pop(),self.b_cards.pop()]
                    a_card = self.b_cards.pop()
                    b_card=self.b_cards.pop()
                  
                elif len(self.b_cards)==1:
                    card_on_stash= card_on_stash + [a_card,b_card,self.a_cards.pop(),self.b_cards.pop()]
                    a_card = self.a_cards.pop()
                    b_card=self.a_cards.pop()
                  
                elif len(self.a_cards)==1:
                    card_on_stash= card_on_stash + [a_card,b_card,self.a_cards.pop(),self.b_cards.pop()]
                    a_card = self.b_cards.pop()
                    b_card=self.b_cards.pop()    
                    
       
            if a_card.get_card_value() > b_card.get_card_value():
                self.a_cards=card_on_stash + [a_card] + [b_card] +self.a_cards
            elif b_card.get_card_value() > a_card.get_card_value():
                self.b_cards=card_on_stash + [a_card] + [b_card]+self.b_cards       
           
            print("round: %s, a_cards: %s, b_cards: %s" %
               (round, len(self.a_cards), len(self.b_cards)))
            round += 1
               
            Once_again=''
            if round>10000:
                print("Too many rounds, shuffling cards and playing one more time")
                Once_again = input('Do you want to play again (Y/N): ').upper()
                if Once_again == 'Y':
                    self.__init__()
                    self.play_war_game()
                else:
                    break
            if Once_again == 'N':
                break
        
def main():
    deck= CardDeck()
    deck.show()  
    
    war_game=War_Game()
    war_game.play_war_game()


main()


