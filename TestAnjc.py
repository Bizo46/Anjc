import unittest
from Anjc import Anjc

class AnjcTestCase(unittest.TestCase):
	def testDeckSize(self):
		gameTest = Anjc()
		deck = gameTest.create_deck()
		self.assertEqual(len(deck), 52, "Deck has 52 cards")

	def testShuffleRandomizesDeck(self):
		gameTest = Anjc()

		deckOne = gameTest.create_deck()
		deckOne = gameTest.shuffle_deck(deckOne)

		deckTwo = gameTest.create_deck()
		deckTwo = gameTest.shuffle_deck(deckTwo)
		
		self.assertNotEqual(str(deckOne), str(deckTwo), "Cards have been shuffled")

	def testDealRemovesACard(self):
		gameTest = Anjc()
		deck = gameTest.create_deck()

		initDeckNum = len(deck)
		gameTest.deal_card(deck)
		afterDealDeckOne = len(deck)

		self.assertEqual(initDeckNum, afterDealDeckOne + 1, "A card is removed")
		
	def testDoesANewCardGetAddedInHand(self):
		gameTest = Anjc()
		deck = gameTest.create_deck()

		hand = gameTest.deal_card(deck)
		self.assertEqual(len(hand), 1, "I need to have 1 card in hand")

		hand = gameTest.add_card_in_hand(hand, deck)
		self.assertEqual(len(hand), 2, "I need to have 2 cards in hand")

	def testSumCardsInSpil(self):
		gameTest = Anjc()
		hand = ["Dama", "Kralj", "Kec"]
		summedCardValues = gameTest.sum_card_values(hand)
		self.assertEqual(summedCardValues, 21, "Card values need to be equal to 21")

	def testValueOfCardsInSpil(self):
		gameTest = Anjc()

		card = gameTest.SPIL["Dama"]
		self.assertEqual(card, 10, "Dama has to be 10")

		card = gameTest.SPIL["Kralj"]
		self.assertEqual(card, 10, "Kralj has to be 10")

		card = gameTest.SPIL["Kec"]
		self.assertEqual(card, 1, "Kec has to be 1")

	def testCardKecValue(self):
		gameTest = Anjc()

		kec = list(gameTest.SPIL.keys())[list(gameTest.SPIL.values()).index(1)]
		self.assertEqual(kec, "Kec", "Kec needs to have a value of 1")

if __name__ == "__main__":
	unittest.main()