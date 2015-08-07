from models import *

for user in User.nodes:
	user.delete()

for card in Card.nodes:
	card.delete()

for deck in Deck.nodes:
	deck.delete()

Sabrina_user=User(name='Sabrina', password='Sabrina').save()

Sabrina_card = Card( name='Sabrina', attributes ={
	'Numero de commits no GitHub':'110'
	,'Tempo de jogo na Steam':'95'
	,'Xicaras cafes por dia':'1'
	,'Bis por dia':'2'
	,'Idade':'33'
	,'Peso':'60'
	,'Horas devidas':'2'
	,'Bananights por mes':'4'
	} ).save()

Dino_user=User(name='Dino', password='Dino').save()

Dino_card = Card( name='Dino', attributes ={
	'Numero de commits no GitHub':'18'
	,'Tempo de jogo na Steam':'960'
	,'Xicaras cafes por dia':'0'
	,'Bis por dia':'7'
	,'Idade':'30'
	,'Peso':'89'
	,'Horas devidas':'8'
	,'Bananights por mes':'4'
	} ).save()

Sereia_user=User(name='Sereia', password='Sereia').save()

Sereia_card = Card( name='Sereia', attributes ={
	'Numero de commits no GitHub':'86'
	,'Tempo de jogo na Steam':'543'
	,'Xicaras cafes por dia':'5'
	,'Bis por dia':'15'
	,'Idade':'32'
	,'Peso':'54'
	,'Horas devidas':'50'
	,'Bananights por mes':'1'
	} ).save()

Mario_user=User(name='Mario', password='Mario').save()

Mario_card = Card( name='Mario', attributes ={
	'Numero de commits no GitHub':'107'
	,'Tempo de jogo na Steam':'618'
	,'Xicaras cafes por dia':'4'
	,'Bis por dia':'10'
	,'Idade':'24'
	,'Peso':'86'
	,'Horas devidas':'44'
	,'Bananights por mes':'8'
	} ).save()

Lucas_user=User(name='Lucas', password='Lucas').save()

Lucas_card = Card( name='Lucas', attributes ={
	'Numero de commits no GitHub':'168'
	,'Tempo de jogo na Steam':'212'
	,'Xicaras cafes por dia':'1'
	,'Bis por dia':'12'
	,'Idade':'30'
	,'Peso':'110'
	,'Horas devidas':'72'
	,'Bananights por mes':'6'
	} ).save()

Aziz_user=User(name='Aziz', password='Aziz').save()

Aziz_card = Card( name='Aziz', attributes ={
	'Numero de commits no GitHub':'132'
	,'Tempo de jogo na Steam':'500'
	,'Xicaras cafes por dia':'0'
	,'Bis por dia':'10'
	,'Idade':'27'
	,'Peso':'142'
	,'Horas devidas':'67'
	,'Bananights por mes':'8'
	} ).save()

Banheiro_user=User(name='Banheiro', password='Banheiro').save()

Banheiro_card = Card( name='Banheiro', attributes ={
	'Numero de commits no GitHub':'50'
	,'Tempo de jogo na Steam':'251'
	,'Xicaras cafes por dia':'4'
	,'Bis por dia':'7'
	,'Idade':'35'
	,'Peso':'70'
	,'Horas devidas':'51'
	,'Bananights por mes':'1'
	} ).save()

Cilo_user=User(name='Cilo', password='Cilo').save()

Cilo_card = Card( name='Cilo', attributes ={
	'Numero de commits no GitHub':'227'
	,'Tempo de jogo na Steam':'430'
	,'Xicaras cafes por dia':'2'
	,'Bis por dia':'6'
	,'Idade':'27'
	,'Peso':'131'
	,'Horas devidas':'51'
	,'Bananights por mes':'5'
	} ).save()

Rui_user=User(name='Rui', password='Rui').save()

Rui_card = Card( name='Rui', attributes ={
	'Numero de commits no GitHub':'54'
	,'Tempo de jogo na Steam':'296'
	,'Xicaras cafes por dia':'6'
	,'Bis por dia':'17'
	,'Idade':'21'
	,'Peso':'112'
	,'Horas devidas':'52'
	,'Bananights por mes':'5'
	} ).save()

Brubs_user=User(name='Brubs', password='Brubs').save()

Brubs_card = Card( name='Brubs', attributes ={
	'Numero de commits no GitHub':'46'
	,'Tempo de jogo na Steam':'973'
	,'Xicaras cafes por dia':'5'
	,'Bis por dia':'6'
	,'Idade':'25'
	,'Peso':'121'
	,'Horas devidas':'64'
	,'Bananights por mes':'7'
	} ).save()

Dezao_user=User(name='Dezao', password='Dezao').save()

Dezao_card = Card( name='Dezao', attributes ={
	'Idade':'13'
	,'Numero de commits no GitHub':'93'
	,'Tempo de jogo na Steam':'209'
	,'Xicaras cafes por dia':'3'
	,'Bis por dia':'18'
	,'Peso':'84'
	,'Horas devidas':'63'
	,'Bananights por mes':'4'
	} ).save()

Solei_user=User(name='Solei', password='Solei').save()

Solei_card = Card( name='Solei', attributes ={
	'Numero de commits no GitHub':'20'
	,'Tempo de jogo na Steam':'852'
	,'Xicaras cafes por dia':'6'
	,'Bis por dia':'16'
	,'Idade':'26'
	,'Peso':'78'
	,'Horas devidas':'81'
	,'Bananights por mes':'3'
	} ).save()

Nheta_user=User(name='Nheta', password='Nheta').save()

Nheta_card = Card( name='Nheta', attributes ={
	'Numero de commits no GitHub':'44'
	,'Tempo de jogo na Steam':'409'
	,'Xicaras cafes por dia':'6'
	,'Bis por dia':'10'
	,'Idade':'20'
	,'Peso':'142'
	,'Horas devidas':'4'
	,'Bananights por mes':'4'
	} ).save()

Soldera_user=User(name='Soldera', password='Soldera').save()

Soldera_card = Card( name='Soldera', attributes ={
	'Numero de commits no GitHub':'6'
	,'Tempo de jogo na Steam':'573'
	,'Xicaras cafes por dia':'5'
	,'Bis por dia':'17'
	,'Idade':'24'
	,'Peso':'124'
	,'Horas devidas':'92'
	,'Bananights por mes':'0'
	} ).save()

Carioca_user=User(name='Carioca', password='Carioca').save()

Carioca_card = Card( name='Carioca', attributes ={
	'Numero de commits no GitHub':'234'
	,'Tempo de jogo na Steam':'270'
	,'Xicaras cafes por dia':'4'
	,'Bis por dia':'16'
	,'Idade':'27'
	,'Peso':'112'
	,'Horas devidas':'57'
	,'Bananights por mes':'5'
	} ).save()

Pila_user=User(name='Pila', password='Pila').save()

Pila_card = Card( name='Pila', attributes ={
	'Numero de commits no GitHub':'239'
	,'Tempo de jogo na Steam':'884'
	,'Xicaras cafes por dia':'6'
	,'Bis por dia':'0'
	,'Idade':'21'
	,'Peso':'141'
	,'Horas devidas':'79'
	,'Bananights por mes':'7'
	} ).save()

Ronaldo_user=User(name='Ronaldo', password='Ronaldo').save()

Ronaldo_card = Card( name='Ronaldo', attributes ={
	'Numero de commits no GitHub':'241'
	,'Tempo de jogo na Steam':'754'
	,'Xicaras cafes por dia':'5'
	,'Bis por dia':'19'
	,'Idade':'20'
	,'Peso':'126'
	,'Horas devidas':'26'
	,'Bananights por mes':'8'
	} ).save()

Theo_user=User(name='Theo', password='Theo').save()

Theo_card = Card( name='Theo', attributes ={
	'Numero de commits no GitHub':'107'
	,'Tempo de jogo na Steam':'398'
	,'Xicaras cafes por dia':'5'
	,'Bis por dia':'9'
	,'Idade':'25'
	,'Peso':'80'
	,'Horas devidas':'87'
	,'Bananights por mes':'8'
	} ).save()

Buzz_user=User(name='Buzz', password='Buzz').save()

Buzz_card = Card( name='Buzz', attributes ={
	'Numero de commits no GitHub':'224'
	,'Tempo de jogo na Steam':'222'
	,'Xicaras cafes por dia':'1'
	,'Bis por dia':'5'
	,'Idade':'36'
	,'Peso':'146'
	,'Horas devidas':'29'
	,'Bananights por mes':'1'
	} ).save()

Sara_user=User(name='Sara', password='Sara').save()

Sara_card = Card( name='Sara', attributes ={
	'Numero de commits no GitHub':'238'
	,'Tempo de jogo na Steam':'518'
	,'Xicaras cafes por dia':'2'
	,'Bis por dia':'5'
	,'Idade':'28'
	,'Peso':'52'
	,'Horas devidas':'7'
	,'Bananights por mes':'2'
	} ).save()

Plato_user=User(name='Plato', password='Plato').save()

Plato_card = Card( name='Plato', attributes ={
	'Numero de commits no GitHub':'19'
	,'Tempo de jogo na Steam':'64'
	,'Xicaras cafes por dia':'1'
	,'Bis por dia':'8'
	,'Idade':'38'
	,'Peso':'144'
	,'Horas devidas':'7'
	,'Bananights por mes':'4'
	} ).save()

TI_deck= Deck( 
name='TI', attributes = [
	'Tempo de jogo na Steam'	,'Xicaras cafes por dia'	,'Bis por dia'	] ).save()

TI_deck.cards.connect(Sabrina_card)
TI_deck.cards.connect(Dino_card)
TI_deck.cards.connect(Sereia_card)
TI_deck.cards.connect(Mario_card)
TI_deck.cards.connect(Lucas_card)
TI_deck.cards.connect(Aziz_card)
TI_deck.cards.connect(Banheiro_card)
TI_deck.cards.connect(Cilo_card)
TI_deck.cards.connect(Rui_card)
TI_deck.cards.connect(Brubs_card)
TI_deck.cards.connect(Dezao_card)
Marketing_deck= Deck( 
name='Marketing', attributes = [
	'Peso'	,'Horas devidas'	,'Bananights por mes'	] ).save()

Marketing_deck.cards.connect(Solei_card)
Marketing_deck.cards.connect(Nheta_card)
Marketing_deck.cards.connect(Soldera_card)
Marketing_deck.cards.connect(Carioca_card)
Marketing_deck.cards.connect(Pila_card)
Marketing_deck.cards.connect(Ronaldo_card)
Marketing_deck.cards.connect(Theo_card)
Marketing_deck.cards.connect(Buzz_card)
Marketing_deck.cards.connect(Sara_card)
Marketing_deck.cards.connect(Plato_card)
