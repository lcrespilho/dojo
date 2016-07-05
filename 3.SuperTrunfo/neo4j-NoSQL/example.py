from models import *

for user in User.nodes:
    user.delete()

user1 = User(name="user1").save()

for card in Card.nodes:
    card.delete()

cards = [Card(name="card%d" % i).save() for i in range(3)]

for deck in Deck.nodes:
    deck.delete()

deck1 = Deck(name="deck1").save()

for card in cards:
    deck1.cards.connect(card)

deck1.owner.connect(user1)

