vals  = ['2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , 'jack' , 'queen' , 'king' , 'ace']
suits = [ 'spades' , 'clubs' , 'hearts' , 'diamonds' ]

#Write a normal function without using lambda, zip, and map function to create 52 cards in a deck
def Deck(list1, list2):
  pack_Deck = [(list1[i], list2[j]) for i in range(0, len(list1)) for j in range(0, len(list2))]
  return pack_Deck

print(Deck(suits,vals))
