from models import *

for user in User.nodes:
    user.delete()


for card in Card.nodes:
    card.delete()

for deck in Deck.nodes:
    deck.delete()


# Users
sudo_user = User(name="sudo", password="haha1212").save()
ariel_user = User(name="ariel", password="ariel").save()

# Cards
dezao_card = Card( name="Dezao", attributes={ "Numero de commits no GitHub":13, # 1 - 300
                "Tempo de jogo na Steam":836, # 1 - 1000
                "Xicaras cafes por dia":2, # 0 - 6
                "Bis por dia":7 # 0 - 20
                } ).save()

ariel_card = Card( name="Ariel",

banheiro_card = Card( name="Banheiro",

#Decks
deck1 = Deck(name="deck1" attributes={ "Numero de commits(GitHub)",
                "steamTime",
                "coffeesPerDay",
                "nBis" } ).save()

).save()

deck1.cards.connect(dezao)

deck1.owner.connect(sudo_user)

