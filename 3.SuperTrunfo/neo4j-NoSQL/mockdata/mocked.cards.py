from models import *

for user in User.nodes:
	user.delete()

for card in Card.nodes:
	card.delete()

for deck in Deck.nodes:
	deck.delete()

Sabrina_user=User(name='Sabrina', password='Sabrina').save()

Sabrina_card = Card( name='Sabrina', attributes ={
	'Numero de commits no GitHub':'1'
	,'Tempo de jogo na Steam':'434'
	,'Xicaras cafes por dia':'2'
	,'Bis por dia':'15'
	,'Idade':'22'
	,'Peso':'120'
	,'Horas devidas':'53'
	,'Bananights por mes':'4'
	} ).save()

Dino_user=User(name='Dino', password='Dino').save()

Dino_card = Card( name='Dino', attributes ={
	'Numero de commits no GitHub':'4'
	,'Tempo de jogo na Steam':'623'
	,'Xicaras cafes por dia':'3'
	,'Bis por dia':'15'
	,'Idade':'23'
	,'Peso':'89'
	,'Horas devidas':'4'
	,'Bananights por mes':'7'
	} ).save()

Sereia_user=User(name='Sereia', password='Sereia').save()

Sereia_card = Card( name='Sereia', attributes ={
	'Numero de commits no GitHub':'220'
	,'Tempo de jogo na Steam':'523'
	,'Xicaras cafes por dia':'5'
	,'Bis por dia':'8'
	,'Idade':'21'
	,'Peso':'127'
	,'Horas devidas':'44'
	,'Bananights por mes':'4'
	} ).save()

Mario_user=User(name='Mario', password='Mario').save()

Mario_card = Card( name='Mario', attributes ={
	'Numero de commits no GitHub':'189'
	,'Tempo de jogo na Steam':'501'
	,'Xicaras cafes por dia':'5'
	,'Bis por dia':'9'
	,'Idade':'22'
	,'Peso':'142'
	,'Horas devidas':'94'
	,'Bananights por mes':'6'
	} ).save()

Lucas_user=User(name='Lucas', password='Lucas').save()

Lucas_card = Card( name='Lucas', attributes ={
	'Numero de commits no GitHub':'72'
	,'Tempo de jogo na Steam':'459'
	,'Xicaras cafes por dia':'1'
	,'Bis por dia':'7'
	,'Idade':'40'
	,'Peso':'114'
	,'Horas devidas':'23'
	,'Bananights por mes':'0'
	} ).save()

Aziz_user=User(name='Aziz', password='Aziz').save()

Aziz_card = Card( name='Aziz', attributes ={
	'Numero de commits no GitHub':'125'
	,'Tempo de jogo na Steam':'469'
	,'Xicaras cafes por dia':'2'
	,'Bis por dia':'8'
	,'Idade':'39'
	,'Peso':'64'
	,'Horas devidas':'50'
	,'Bananights por mes':'4'
	} ).save()

Banheiro_user=User(name='Banheiro', password='Banheiro').save()

Banheiro_card = Card( name='Banheiro', attributes ={
	'Numero de commits no GitHub':'80'
	,'Tempo de jogo na Steam':'597'
	,'Xicaras cafes por dia':'0'
	,'Bis por dia':'19'
	,'Idade':'39'
	,'Peso':'61'
	,'Horas devidas':'73'
	,'Bananights por mes':'1'
	} ).save()

Cilo_user=User(name='Cilo', password='Cilo').save()

Cilo_card = Card( name='Cilo', attributes ={
	'Numero de commits no GitHub':'177'
	,'Tempo de jogo na Steam':'484'
	,'Xicaras cafes por dia':'0'
	,'Bis por dia':'6'
	,'Idade':'32'
	,'Peso':'136'
	,'Horas devidas':'71'
	,'Bananights por mes':'4'
	} ).save()

Rui_user=User(name='Rui', password='Rui').save()

Rui_card = Card( name='Rui', attributes ={
	'Numero de commits no GitHub':'10'
	,'Tempo de jogo na Steam':'262'
	,'Xicaras cafes por dia':'0'
	,'Bis por dia':'20'
	,'Idade':'25'
	,'Peso':'138'
	,'Horas devidas':'45'
	,'Bananights por mes':'0'
	} ).save()

Brubs_user=User(name='Brubs', password='Brubs').save()

Brubs_card = Card( name='Brubs', attributes ={
	'Numero de commits no GitHub':'236'
	,'Tempo de jogo na Steam':'968'
	,'Xicaras cafes por dia':'5'
	,'Bis por dia':'13'
	,'Idade':'27'
	,'Peso':'148'
	,'Horas devidas':'0'
	,'Bananights por mes':'8'
	} ).save()

Dezao_user=User(name='Dezao', password='Dezao').save()

Dezao_card = Card( name='Dezao', attributes ={
	'Idade':'13'
	,'Numero de commits no GitHub':'195'
	,'Tempo de jogo na Steam':'86'
	,'Xicaras cafes por dia':'0'
	,'Bis por dia':'9'
	,'Peso':'141'
	,'Horas devidas':'91'
	,'Bananights por mes':'5'
	} ).save()

Solei_user=User(name='Solei', password='Solei').save()

Solei_card = Card( name='Solei', attributes ={
	'Numero de commits no GitHub':'34'
	,'Tempo de jogo na Steam':'630'
	,'Xicaras cafes por dia':'6'
	,'Bis por dia':'19'
	,'Idade':'26'
	,'Peso':'115'
	,'Horas devidas':'84'
	,'Bananights por mes':'0'
	} ).save()

Nheta_user=User(name='Nheta', password='Nheta').save()

Nheta_card = Card( name='Nheta', attributes ={
	'Numero de commits no GitHub':'267'
	,'Tempo de jogo na Steam':'305'
	,'Xicaras cafes por dia':'6'
	,'Bis por dia':'16'
	,'Idade':'22'
	,'Peso':'99'
	,'Horas devidas':'70'
	,'Bananights por mes':'8'
	} ).save()

Soldera_user=User(name='Soldera', password='Soldera').save()

Soldera_card = Card( name='Soldera', attributes ={
	'Numero de commits no GitHub':'233'
	,'Tempo de jogo na Steam':'747'
	,'Xicaras cafes por dia':'0'
	,'Bis por dia':'13'
	,'Idade':'32'
	,'Peso':'134'
	,'Horas devidas':'87'
	,'Bananights por mes':'1'
	} ).save()

Carioca_user=User(name='Carioca', password='Carioca').save()

Carioca_card = Card( name='Carioca', attributes ={
	'Numero de commits no GitHub':'158'
	,'Tempo de jogo na Steam':'55'
	,'Xicaras cafes por dia':'6'
	,'Bis por dia':'7'
	,'Idade':'27'
	,'Peso':'108'
	,'Horas devidas':'67'
	,'Bananights por mes':'4'
	} ).save()

Pila_user=User(name='Pila', password='Pila').save()

Pila_card = Card( name='Pila', attributes ={
	'Numero de commits no GitHub':'22'
	,'Tempo de jogo na Steam':'942'
	,'Xicaras cafes por dia':'6'
	,'Bis por dia':'6'
	,'Idade':'26'
	,'Peso':'105'
	,'Horas devidas':'65'
	,'Bananights por mes':'3'
	} ).save()

Ronaldo_user=User(name='Ronaldo', password='Ronaldo').save()

Ronaldo_card = Card( name='Ronaldo', attributes ={
	'Numero de commits no GitHub':'167'
	,'Tempo de jogo na Steam':'48'
	,'Xicaras cafes por dia':'6'
	,'Bis por dia':'19'
	,'Idade':'36'
	,'Peso':'142'
	,'Horas devidas':'78'
	,'Bananights por mes':'1'
	} ).save()

Theo_user=User(name='Theo', password='Theo').save()

Theo_card = Card( name='Theo', attributes ={
	'Numero de commits no GitHub':'121'
	,'Tempo de jogo na Steam':'46'
	,'Xicaras cafes por dia':'3'
	,'Bis por dia':'1'
	,'Idade':'32'
	,'Peso':'110'
	,'Horas devidas':'40'
	,'Bananights por mes':'5'
	} ).save()

Buzz_user=User(name='Buzz', password='Buzz').save()

Buzz_card = Card( name='Buzz', attributes ={
	'Numero de commits no GitHub':'132'
	,'Tempo de jogo na Steam':'717'
	,'Xicaras cafes por dia':'2'
	,'Bis por dia':'0'
	,'Idade':'37'
	,'Peso':'73'
	,'Horas devidas':'8'
	,'Bananights por mes':'3'
	} ).save()

Sara_user=User(name='Sara', password='Sara').save()

Sara_card = Card( name='Sara', attributes ={
	'Numero de commits no GitHub':'273'
	,'Tempo de jogo na Steam':'363'
	,'Xicaras cafes por dia':'1'
	,'Bis por dia':'11'
	,'Idade':'19'
	,'Peso':'86'
	,'Horas devidas':'31'
	,'Bananights por mes':'2'
	} ).save()

Plato_user=User(name='Plato', password='Plato').save()

Plato_card = Card( name='Plato', attributes ={
	'Numero de commits no GitHub':'44'
	,'Tempo de jogo na Steam':'659'
	,'Xicaras cafes por dia':'1'
	,'Bis por dia':'19'
	,'Idade':'29'
	,'Peso':'75'
	,'Horas devidas':'19'
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
