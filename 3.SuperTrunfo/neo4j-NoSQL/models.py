import neomodel as nm

class User(nm.StructuredNode):
    name = nm.StringProperty(unique_index=True)
    password = nm.StringProperty()

class Card(nm.StructuredNode):
    name = nm.StringProperty(unique_index=True)
    attributes = nm.JSONProperty()

class Deck(nm.StructuredNode):
    name = nm.StringProperty(unique_index=True)
    cards = nm.RelationshipTo('Card', 'CARD')
    owner = nm.RelationshipFrom('User', 'USER', cardinality=nm.One)
    attributes = nm.JSONProperty()




