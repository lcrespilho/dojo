from models import *

for user in User.nodes:
	user.delete()

for card in Card.nodes:
	card.delete()

for deck in Deck.nodes:
	deck.delete()

Sabrina_card = Card( name='Sabrina', attributes ={
	'Numero de commits no GitHub':'155'
	,'Tempo de jogo na Steam':'551'
	,'Xicaras cafes por dia':'4'
	,'Bis por dia':'6'
	,'Idade':'31'
	,'Peso':'132'
	,'Horas devidas':'78'
	,'Bananights por mes':'6'
	} ).save()

Dino_card = Card( name='Dino', attributes ={
	'Numero de commits no GitHub':'231'
	,'Tempo de jogo na Steam':'766'
	,'Xicaras cafes por dia':'2'
	,'Bis por dia':'9'
	,'Idade':'40'
	,'Peso':'86'
	,'Horas devidas':'62'
	,'Bananights por mes':'8'
	} ).save()

Sereia_card = Card( name='Sereia', attributes ={
	'Numero de commits no GitHub':'187'
	,'Tempo de jogo na Steam':'818'
	,'Xicaras cafes por dia':'0'
	,'Bis por dia':'13'
	,'Idade':'31'
	,'Peso':'79'
	,'Horas devidas':'56'
	,'Bananights por mes':'8'
	} ).save()

Mario_card = Card( name='Mario', attributes ={
	'Numero de commits no GitHub':'86'
	,'Tempo de jogo na Steam':'253'
	,'Xicaras cafes por dia':'4'
	,'Bis por dia':'7'
	,'Idade':'19'
	,'Peso':'133'
	,'Horas devidas':'67'
	,'Bananights por mes':'8'
	} ).save()

Lucas_card = Card( name='Lucas', attributes ={
	'Numero de commits no GitHub':'256'
	,'Tempo de jogo na Steam':'637'
	,'Xicaras cafes por dia':'6'
	,'Bis por dia':'16'
	,'Idade':'18'
	,'Peso':'108'
	,'Horas devidas':'36'
	,'Bananights por mes':'4'
	} ).save()

Aziz_card = Card( name='Aziz', attributes ={
	'Numero de commits no GitHub':'19'
	,'Tempo de jogo na Steam':'248'
	,'Xicaras cafes por dia':'1'
	,'Bis por dia':'13'
	,'Idade':'38'
	,'Peso':'79'
	,'Horas devidas':'11'
	,'Bananights por mes':'7'
	} ).save()

Banheiro_card = Card( name='Banheiro', attributes ={
	'Numero de commits no GitHub':'50'
	,'Tempo de jogo na Steam':'346'
	,'Xicaras cafes por dia':'3'
	,'Bis por dia':'20'
	,'Idade':'21'
	,'Peso':'52'
	,'Horas devidas':'52'
	,'Bananights por mes':'3'
	} ).save()

Cilo_card = Card( name='Cilo', attributes ={
	'Numero de commits no GitHub':'122'
	,'Tempo de jogo na Steam':'229'
	,'Xicaras cafes por dia':'5'
	,'Bis por dia':'5'
	,'Idade':'38'
	,'Peso':'123'
	,'Horas devidas':'76'
	,'Bananights por mes':'0'
	} ).save()

Rui_card = Card( name='Rui', attributes ={
	'Numero de commits no GitHub':'176'
	,'Tempo de jogo na Steam':'683'
	,'Xicaras cafes por dia':'3'
	,'Bis por dia':'5'
	,'Idade':'32'
	,'Peso':'138'
	,'Horas devidas':'80'
	,'Bananights por mes':'4'
	} ).save()

Brubs_card = Card( name='Brubs', attributes ={
	'Numero de commits no GitHub':'85'
	,'Tempo de jogo na Steam':'150'
	,'Xicaras cafes por dia':'0'
	,'Bis por dia':'14'
	,'Idade':'29'
	,'Peso':'54'
	,'Horas devidas':'95'
	,'Bananights por mes':'2'
	} ).save()

Dezao_card = Card( name='Dezao', attributes ={
	'Idade':'13'
	,'Numero de commits no GitHub':'158'
	,'Tempo de jogo na Steam':'876'
	,'Xicaras cafes por dia':'3'
	,'Bis por dia':'13'
	,'Peso':'74'
	,'Horas devidas':'93'
	,'Bananights por mes':'2'
	} ).save()

Solei_card = Card( name='Solei', attributes ={
	'Peso':'258'
	,'Numero de commits no GitHub':'20'
	,'Tempo de jogo na Steam':'167'
	,'Xicaras cafes por dia':'5'
	,'Bis por dia':'2'
	,'Idade':'25'
	,'Horas devidas':'58'
	,'Bananights por mes':'3'
	} ).save()

Nheta_card = Card( name='Nheta', attributes ={
	'Numero de commits no GitHub':'260'
	,'Tempo de jogo na Steam':'510'
	,'Xicaras cafes por dia':'6'
	,'Bis por dia':'2'
	,'Idade':'26'
	,'Peso':'134'
	,'Horas devidas':'64'
	,'Bananights por mes':'1'
	} ).save()

Soldera_card = Card( name='Soldera', attributes ={
	'Numero de commits no GitHub':'120'
	,'Tempo de jogo na Steam':'319'
	,'Xicaras cafes por dia':'4'
	,'Bis por dia':'19'
	,'Idade':'38'
	,'Peso':'115'
	,'Horas devidas':'80'
	,'Bananights por mes':'7'
	} ).save()

Tulio_card = Card( name='Tulio', attributes ={
	'Numero de commits no GitHub':'241'
	,'Tempo de jogo na Steam':'154'
	,'Xicaras cafes por dia':'4'
	,'Bis por dia':'9'
	,'Idade':'30'
	,'Peso':'67'
	,'Horas devidas':'75'
	,'Bananights por mes':'0'
	} ).save()

Andre_card = Card( name='Andre', attributes ={
	'Numero de commits no GitHub':'204'
	,'Tempo de jogo na Steam':'706'
	,'Xicaras cafes por dia':'0'
	,'Bis por dia':'20'
	,'Idade':'31'
	,'Peso':'62'
	,'Horas devidas':'43'
	,'Bananights por mes':'3'
	} ).save()

Carioca_card = Card( name='Carioca', attributes ={
	'Numero de commits no GitHub':'75'
	,'Tempo de jogo na Steam':'936'
	,'Xicaras cafes por dia':'4'
	,'Bis por dia':'2'
	,'Idade':'36'
	,'Peso':'124'
	,'Horas devidas':'13'
	,'Bananights por mes':'2'
	} ).save()

Pila_card = Card( name='Pila', attributes ={
	'Numero de commits no GitHub':'280'
	,'Tempo de jogo na Steam':'273'
	,'Xicaras cafes por dia':'3'
	,'Bis por dia':'8'
	,'Idade':'40'
	,'Peso':'112'
	,'Horas devidas':'24'
	,'Bananights por mes':'0'
	} ).save()

Ronaldo_card = Card( name='Ronaldo', attributes ={
	'Numero de commits no GitHub':'135'
	,'Tempo de jogo na Steam':'355'
	,'Xicaras cafes por dia':'6'
	,'Bis por dia':'19'
	,'Idade':'36'
	,'Peso':'142'
	,'Horas devidas':'11'
	,'Bananights por mes':'5'
	} ).save()

Theo_card = Card( name='Theo', attributes ={
	'Numero de commits no GitHub':'70'
	,'Tempo de jogo na Steam':'874'
	,'Xicaras cafes por dia':'3'
	,'Bis por dia':'12'
	,'Idade':'19'
	,'Peso':'120'
	,'Horas devidas':'4'
	,'Bananights por mes':'4'
	} ).save()

Buzz_card = Card( name='Buzz', attributes ={
	'Numero de commits no GitHub':'167'
	,'Tempo de jogo na Steam':'933'
	,'Xicaras cafes por dia':'6'
	,'Bis por dia':'18'
	,'Idade':'34'
	,'Peso':'55'
	,'Horas devidas':'88'
	,'Bananights por mes':'3'
	} ).save()

Sara_card = Card( name='Sara', attributes ={
	'Numero de commits no GitHub':'10'
	,'Tempo de jogo na Steam':'862'
	,'Xicaras cafes por dia':'5'
	,'Bis por dia':'8'
	,'Idade':'39'
	,'Peso':'149'
	,'Horas devidas':'82'
	,'Bananights por mes':'2'
	} ).save()

Plato_card = Card( name='Plato', attributes ={
	'Numero de commits no GitHub':'145'
	,'Tempo de jogo na Steam':'86'
	,'Xicaras cafes por dia':'4'
	,'Bis por dia':'13'
	,'Idade':'31'
	,'Peso':'67'
	,'Horas devidas':'69'
	,'Bananights por mes':'1'
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
