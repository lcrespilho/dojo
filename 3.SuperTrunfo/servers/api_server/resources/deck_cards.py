import neomodel as nm
from api_server.common.views import BaseListView, BaseDetailView
from .card import BaseCardView, Card
from .deck import Deck
from flask_restful import abort

""" MODEL """

""" VIEWS """


class DeckCardsListView(BaseCardView, BaseListView):
    def get(self, deck_pk):
        try:
            result = [self.serialize(node) for node in Deck.nodes.get(name=deck_pk).cards]
        except nm.DoesNotExist:
            abort(404)

        return result


class DeckCardsDetailView(BaseCardView, BaseDetailView):
    def post(self, deck_pk, card_pk):

        try:
            result_deck = Deck.nodes.get(name=deck_pk)
            result_card = Card.nodes.get(name=card_pk)
            result = result_deck.cards.connect(result_card)

        except nm.DoesNotExist:
            abort(404)

        except:
            abort(400)

        if not result:
            abort(400)

        return "", 201

