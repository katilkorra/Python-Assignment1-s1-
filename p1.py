#1.A card is drawn at random from a deck of well-shuffled cards. Find the probability of it being neither a king nor a spade.

Cards=52
Kings=4
spade=13

neither=Cards-(Kings+spade-1)
probability=neither/Cards
print('Probability of neither king nor spade, is',probability)