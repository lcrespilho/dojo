from models import *

for user in User.nodes:
    user.delete()


for card in Card.nodes:
    card.delete()

for deck in Deck.nodes:
    deck.delete()


# Users
sudo_user = User(name="su", password="haha1212").save()
ariel_user = User(name="ariel", password="ariel").save()

# Cards
dezao_card = Card( name="Dezao", attributes={ "gitCommits":13,
                "steamTime":836,
                "coffeesPerDay":2,
                "nBis":7 } ).save()

ariel_card = Card( name="Ariel", attributes={ "gitCommits":252,
                "steamTime":2710,
                "coffeesPerDay":2,
                "nBis":6 } ).save()

banheiro_card = Card( name="Banheiro", attributes={ "gitCommits":7,
                "steamTime":2710,
                "coffeesPerDay":2,
                "nBis":6 } ).save()

#Decks
deck1 = Deck(name="deck1" attributes={ "gitCommits",
                "steamTime",
                "coffeesPerDay",
                "nBis" } ).save()

).save()

deck1.cards.connect(dezao)

deck1.owner.connect(sudo_user)

