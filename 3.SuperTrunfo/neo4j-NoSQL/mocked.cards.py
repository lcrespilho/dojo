from models import *

for user in User.nodes:
	user.delete()

for card in Card.nodes:
	card.delete()

for deck in Deck.nodes:
	deck.delete()

Sabrina_card = Card( name='Sabrina', attributes ={
	'Numero de commits no GitHub':'181'
	,'Tempo de jogo na Steam':'789'
	,'Xicaras cafes por dia':'6'
	,'Bis por dia':'20'
	,'Idade':'36'
	,'Peso':'96'
	,'Horas devidas':'39'
	,'Bananights por mes':'8'
	} ).save()

Dino_card = Card( name='Dino', attributes ={
	'Numero de commits no GitHub':'153'
	,'Tempo de jogo na Steam':'727'
	,'Xicaras cafes por dia':'1'
	,'Bis por dia':'6'
	,'Idade':'21'
	,'Peso':'141'
	,'Horas devidas':'64'
	,'Bananights por mes':'0'
	} ).save()

Sereia_card = Card( name='Sereia', attributes ={
	'Numero de commits no GitHub':'269'
	,'Tempo de jogo na Steam':'127'
	,'Xicaras cafes por dia':'2'
	,'Bis por dia':'5'
	,'Idade':'23'
	,'Peso':'78'
	,'Horas devidas':'41'
	,'Bananights por mes':'3'
	} ).save()

Mario_card = Card( name='Mario', attributes ={
	'Numero de commits no GitHub':'55'
	,'Tempo de jogo na Steam':'888'
	,'Xicaras cafes por dia':'0'
	,'Bis por dia':'4'
	,'Idade':'35'
	,'Peso':'106'
	,'Horas devidas':'29'
	,'Bananights por mes':'6'
	} ).save()

Lucas_card = Card( name='Lucas', attributes ={
	'Numero de commits no GitHub':'233'
	,'Tempo de jogo na Steam':'861'
	,'Xicaras cafes por dia':'4'
	,'Bis por dia':'18'
	,'Idade':'33'
	,'Peso':'115'
	,'Horas devidas':'17'
	,'Bananights por mes':'4'
	} ).save()

Aziz_card = Card( name='Aziz', attributes ={
	'Numero de commits no GitHub':'144'
	,'Tempo de jogo na Steam':'224'
	,'Xicaras cafes por dia':'0'
	,'Bis por dia':'1'
	,'Idade':'33'
	,'Peso':'57'
	,'Horas devidas':'69'
	,'Bananights por mes':'4'
	} ).save()

Banheiro_card = Card( name='Banheiro', attributes ={
	'Numero de commits no GitHub':'150'
	,'Tempo de jogo na Steam':'731'
	,'Xicaras cafes por dia':'0'
	,'Bis por dia':'19'
	,'Idade':'23'
	,'Peso':'93'
	,'Horas devidas':'45'
	,'Bananights por mes':'5'
	} ).save()

Cilo_card = Card( name='Cilo', attributes ={
	'Numero de commits no GitHub':'78'
	,'Tempo de jogo na Steam':'710'
	,'Xicaras cafes por dia':'1'
	,'Bis por dia':'3'
	,'Idade':'26'
	,'Peso':'77'
	,'Horas devidas':'88'
	,'Bananights por mes':'2'
	} ).save()

Rui_card = Card( name='Rui', attributes ={
	'Numero de commits no GitHub':'222'
	,'Tempo de jogo na Steam':'548'
	,'Xicaras cafes por dia':'3'
	,'Bis por dia':'12'
	,'Idade':'27'
	,'Peso':'75'
	,'Horas devidas':'33'
	,'Bananights por mes':'3'
	} ).save()

Brubs_card = Card( name='Brubs', attributes ={
	'Numero de commits no GitHub':'247'
	,'Tempo de jogo na Steam':'416'
	,'Xicaras cafes por dia':'1'
	,'Bis por dia':'1'
	,'Idade':'33'
	,'Peso':'62'
	,'Horas devidas':'38'
	,'Bananights por mes':'5'
	} ).save()

Dezao_card = Card( name='Dezao', attributes ={
	'Idade':'13'
	,'Numero de commits no GitHub':'282'
	,'Tempo de jogo na Steam':'167'
	,'Xicaras cafes por dia':'4'
	,'Bis por dia':'1'
	,'Peso':'150'
	,'Horas devidas':'61'
	,'Bananights por mes':'7'
	} ).save()

Solei_card = Card( name='Solei', attributes ={
	'Peso':'258'
	,'Numero de commits no GitHub':'273'
	,'Tempo de jogo na Steam':'625'
	,'Xicaras cafes por dia':'4'
	,'Bis por dia':'7'
	,'Idade':'24'
	,'Horas devidas':'14'
	,'Bananights por mes':'4'
	} ).save()

Nheta_card = Card( name='Nheta', attributes ={
	'Numero de commits no GitHub':'72'
	,'Tempo de jogo na Steam':'888'
	,'Xicaras cafes por dia':'1'
	,'Bis por dia':'17'
	,'Idade':'39'
	,'Peso':'67'
	,'Horas devidas':'85'
	,'Bananights por mes':'4'
	} ).save()

Soldera_card = Card( name='Soldera', attributes ={
	'Numero de commits no GitHub':'155'
	,'Tempo de jogo na Steam':'467'
	,'Xicaras cafes por dia':'2'
	,'Bis por dia':'10'
	,'Idade':'23'
	,'Peso':'132'
	,'Horas devidas':'40'
	,'Bananights por mes':'2'
	} ).save()

Tulio_card = Card( name='Tulio', attributes ={
	'Numero de commits no GitHub':'52'
	,'Tempo de jogo na Steam':'882'
	,'Xicaras cafes por dia':'6'
	,'Bis por dia':'2'
	,'Idade':'37'
	,'Peso':'116'
	,'Horas devidas':'7'
	,'Bananights por mes':'0'
	} ).save()

Andre_card = Card( name='Andre', attributes ={
	'Numero de commits no GitHub':'70'
	,'Tempo de jogo na Steam':'748'
	,'Xicaras cafes por dia':'6'
	,'Bis por dia':'9'
	,'Idade':'33'
	,'Peso':'51'
	,'Horas devidas':'24'
	,'Bananights por mes':'7'
	} ).save()

Carioca_card = Card( name='Carioca', attributes ={
	'Numero de commits no GitHub':'297'
	,'Tempo de jogo na Steam':'129'
	,'Xicaras cafes por dia':'6'
	,'Bis por dia':'1'
	,'Idade':'21'
	,'Peso':'79'
	,'Horas devidas':'48'
	,'Bananights por mes':'8'
	} ).save()

Pila_card = Card( name='Pila', attributes ={
	'Numero de commits no GitHub':'221'
	,'Tempo de jogo na Steam':'563'
	,'Xicaras cafes por dia':'3'
	,'Bis por dia':'10'
	,'Idade':'24'
	,'Peso':'102'
	,'Horas devidas':'14'
	,'Bananights por mes':'1'
	} ).save()

Ronaldo_card = Card( name='Ronaldo', attributes ={
	'Numero de commits no GitHub':'4'
	,'Tempo de jogo na Steam':'422'
	,'Xicaras cafes por dia':'0'
	,'Bis por dia':'6'
	,'Idade':'31'
	,'Peso':'119'
	,'Horas devidas':'51'
	,'Bananights por mes':'5'
	} ).save()

Theo_card = Card( name='Theo', attributes ={
	'Numero de commits no GitHub':'96'
	,'Tempo de jogo na Steam':'854'
	,'Xicaras cafes por dia':'5'
	,'Bis por dia':'2'
	,'Idade':'33'
	,'Peso':'54'
	,'Horas devidas':'65'
	,'Bananights por mes':'6'
	} ).save()

Buzz_card = Card( name='Buzz', attributes ={
	'Numero de commits no GitHub':'286'
	,'Tempo de jogo na Steam':'175'
	,'Xicaras cafes por dia':'2'
	,'Bis por dia':'12'
	,'Idade':'34'
	,'Peso':'51'
	,'Horas devidas':'80'
	,'Bananights por mes':'5'
	} ).save()

Sara_card = Card( name='Sara', attributes ={
	'Numero de commits no GitHub':'291'
	,'Tempo de jogo na Steam':'149'
	,'Xicaras cafes por dia':'0'
	,'Bis por dia':'2'
	,'Idade':'40'
	,'Peso':'76'
	,'Horas devidas':'43'
	,'Bananights por mes':'6'
	} ).save()

Plato_card = Card( name='Plato', attributes ={
	'Numero de commits no GitHub':'288'
	,'Tempo de jogo na Steam':'964'
	,'Xicaras cafes por dia':'4'
	,'Bis por dia':'9'
	,'Idade':'18'
	,'Peso':'92'
	,'Horas devidas':'47'
	,'Bananights por mes':'5'
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
	'Peso'	,'Horas devidas'	,'Bananights por mes'	,''	] ).save()

Marketing_deck.cards.connect(Solei_card)
Marketing_deck.cards.connect(Nheta_card)
Marketing_deck.cards.connect(Soldera_card)
Marketing_deck.cards.connect(Tulio_card)
Marketing_deck.cards.connect(Andre_card)
Marketing_deck.cards.connect(Carioca_card)
Marketing_deck.cards.connect(Pila_card)
Marketing_deck.cards.connect(Ronaldo_card)
Marketing_deck.cards.connect(Theo_card)
Marketing_deck.cards.connect(Buzz_card)
Marketing_deck.cards.connect(Sara_card)
Marketing_deck.cards.connect(Plato_card)
