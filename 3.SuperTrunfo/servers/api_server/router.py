from servers.api_server import api
from .resources import card, deck, deck_cards, user, session


_base = '/dojo/'


def define_routes():
    api.add_resource(card.CardListView, _base + 'cards', methods=['GET', 'POST'])
    api.add_resource(card.CardDetailView, _base + 'cards/<string:pk>', methods=['GET', 'PATCH', 'DELETE'])
    api.add_resource(deck.DeckListView, _base + 'decks', methods=['GET', 'POST'])
    api.add_resource(deck.DeckDetailView, _base + 'decks/<string:pk>', methods=['GET', 'PATCH', 'DELETE'])
    api.add_resource(deck_cards.DeckCardsListView, _base + 'decks/<string:deck_pk>/cards', methods=['GET'])
    api.add_resource(deck_cards.DeckCardsDetailView, _base + 'decks/<string:deck_pk>/cards/<string:card_pk>',
                     methods=['GET', 'POST'])
    api.add_resource(user.UserListView, _base + 'users', methods=['GET', 'POST'])
    api.add_resource(user.UserDetailView, _base + 'users/<string:pk>', methods=['GET', 'PATCH', 'DELETE'])

    api.add_resource(session.SessionListView, _base + 'game_sessions', methods=['GET', 'POST'])
