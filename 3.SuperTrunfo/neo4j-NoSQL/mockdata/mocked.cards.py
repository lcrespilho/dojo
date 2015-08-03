from models import *

for user in User.nodes:
	user.delete()

for card in Card.nodes:
	card.delete()

for deck in Deck.nodes:
	deck.delete()

Sabrina_user=User(name='Sabrina', password='Sabrina').save()

Sabrina_card = Card( name='Sabrina', attributes ={
	'Numero de commits no GitHub':'108'
	,'Tempo de jogo na Steam':'845'
	,'Xicaras cafes por dia':'2'
	,'Bis por dia':'11'
	,'Idade':'39'
	,'Peso':'147'
	,'Horas devidas':'41'
	,'Bananights por mes':'2'
	} ).save()

Dino_user=User(name='Dino', password='Dino').save()

Dino_card = Card( name='Dino', attributes ={
	'Numero de commits no GitHub':'89'
	,'Tempo de jogo na Steam':'265'
	,'Xicaras cafes por dia':'1'
	,'Bis por dia':'1'
	,'Idade':'28'
	,'Peso':'60'
	,'Horas devidas':'43'
	,'Bananights por mes':'5'
	} ).save()

Sereia_user=User(name='Sereia', password='Sereia').save()

Sereia_card = Card( name='Sereia', attributes ={
	'Numero de commits no GitHub':'136'
	,'Tempo de jogo na Steam':'367'
	,'Xicaras cafes por dia':'3'
	,'Bis por dia':'10'
	,'Idade':'20'
	,'Peso':'69'
	,'Horas devidas':'25'
	,'Bananights por mes':'3'
	} ).save()

Mario_user=User(name='Mario', password='Mario').save()

Mario_card = Card( name='Mario', attributes ={
	'Numero de commits no GitHub':'217'
	,'Tempo de jogo na Steam':'276'
	,'Xicaras cafes por dia':'4'
	,'Bis por dia':'7'
	,'Idade':'21'
	,'Peso':'62'
	,'Horas devidas':'77'
	,'Bananights por mes':'8'
	} ).save()

Lucas_user=User(name='Lucas', password='Lucas').save()

Lucas_card = Card( name='Lucas', attributes ={
	'Numero de commits no GitHub':'279'
	,'Tempo de jogo na Steam':'112'
	,'Xicaras cafes por dia':'4'
	,'Bis por dia':'9'
	,'Idade':'29'
	,'Peso':'73'
	,'Horas devidas':'64'
	,'Bananights por mes':'2'
	} ).save()

Aziz_user=User(name='Aziz', password='Aziz').save()

Aziz_card = Card( name='Aziz', attributes ={
	'Numero de commits no GitHub':'253'
	,'Tempo de jogo na Steam':'163'
	,'Xicaras cafes por dia':'3'
	,'Bis por dia':'20'
	,'Idade':'28'
	,'Peso':'133'
	,'Horas devidas':'28'
	,'Bananights por mes':'4'
	} ).save()

Banheiro_user=User(name='Banheiro', password='Banheiro').save()

Banheiro_card = Card( name='Banheiro', attributes ={
	'Numero de commits no GitHub':'153'
	,'Tempo de jogo na Steam':'586'
	,'Xicaras cafes por dia':'2'
	,'Bis por dia':'2'
	,'Idade':'25'
	,'Peso':'132'
	,'Horas devidas':'20'
	,'Bananights por mes':'7'
	} ).save()

Cilo_user=User(name='Cilo', password='Cilo').save()

Cilo_card = Card( name='Cilo', attributes ={
	'Numero de commits no GitHub':'63'
	,'Tempo de jogo na Steam':'555'
	,'Xicaras cafes por dia':'0'
	,'Bis por dia':'2'
	,'Idade':'30'
	,'Peso':'77'
	,'Horas devidas':'2'
	,'Bananights por mes':'0'
	} ).save()

Rui_user=User(name='Rui', password='Rui').save()

Rui_card = Card( name='Rui', attributes ={
	'Numero de commits no GitHub':'45'
	,'Tempo de jogo na Steam':'750'
	,'Xicaras cafes por dia':'6'
	,'Bis por dia':'19'
	,'Idade':'28'
	,'Peso':'59'
	,'Horas devidas':'28'
	,'Bananights por mes':'0'
	} ).save()

Brubs_user=User(name='Brubs', password='Brubs').save()

Brubs_card = Card( name='Brubs', attributes ={
	'Numero de commits no GitHub':'258'
	,'Tempo de jogo na Steam':'625'
	,'Xicaras cafes por dia':'2'
	,'Bis por dia':'4'
	,'Idade':'40'
	,'Peso':'79'
	,'Horas devidas':'70'
	,'Bananights por mes':'8'
	} ).save()

Dezao_user=User(name='Dezao', password='Dezao').save()

Dezao_card = Card( name='Dezao', attributes ={
	'Idade':'13'
	,'Numero de commits no GitHub':'119'
	,'Tempo de jogo na Steam':'542'
	,'Xicaras cafes por dia':'6'
	,'Bis por dia':'0'
	,'Peso':'148'
	,'Horas devidas':'21'
	,'Bananights por mes':'4'
	} ).save()

Solei_user=User(name='Solei', password='Solei').save()

Solei_card = Card( name='Solei', attributes ={
	'Numero de commits no GitHub':'110'
	,'Tempo de jogo na Steam':'561'
	,'Xicaras cafes por dia':'5'
	,'Bis por dia':'18'
	,'Idade':'39'
	,'Peso':'74'
	,'Horas devidas':'57'
	,'Bananights por mes':'0'
	} ).save()

Nheta_user=User(name='Nheta', password='Nheta').save()

Nheta_card = Card( name='Nheta', attributes ={
	'Numero de commits no GitHub':'260'
	,'Tempo de jogo na Steam':'15'
	,'Xicaras cafes por dia':'3'
	,'Bis por dia':'19'
	,'Idade':'25'
	,'Peso':'81'
	,'Horas devidas':'33'
	,'Bananights por mes':'5'
	} ).save()

Soldera_user=User(name='Soldera', password='Soldera').save()

Soldera_card = Card( name='Soldera', attributes ={
	'Numero de commits no GitHub':'40'
	,'Tempo de jogo na Steam':'127'
	,'Xicaras cafes por dia':'4'
	,'Bis por dia':'19'
	,'Idade':'28'
	,'Peso':'108'
	,'Horas devidas':'87'
	,'Bananights por mes':'3'
	} ).save()

Carioca_user=User(name='Carioca', password='Carioca').save()

Carioca_card = Card( name='Carioca', attributes ={
	'Numero de commits no GitHub':'229'
	,'Tempo de jogo na Steam':'840'
	,'Xicaras cafes por dia':'0'
	,'Bis por dia':'12'
	,'Idade':'32'
	,'Peso':'136'
	,'Horas devidas':'91'
	,'Bananights por mes':'5'
	} ).save()

Pila_user=User(name='Pila', password='Pila').save()

Pila_card = Card( name='Pila', attributes ={
	'Numero de commits no GitHub':'67'
	,'Tempo de jogo na Steam':'745'
	,'Xicaras cafes por dia':'5'
	,'Bis por dia':'16'
	,'Idade':'39'
	,'Peso':'91'
	,'Horas devidas':'92'
	,'Bananights por mes':'4'
	} ).save()

Ronaldo_user=User(name='Ronaldo', password='Ronaldo').save()

Ronaldo_card = Card( name='Ronaldo', attributes ={
	'Numero de commits no GitHub':'150'
	,'Tempo de jogo na Steam':'340'
	,'Xicaras cafes por dia':'5'
	,'Bis por dia':'14'
	,'Idade':'23'
	,'Peso':'83'
	,'Horas devidas':'91'
	,'Bananights por mes':'8'
	} ).save()

Theo_user=User(name='Theo', password='Theo').save()

Theo_card = Card( name='Theo', attributes ={
	'Numero de commits no GitHub':'120'
	,'Tempo de jogo na Steam':'276'
	,'Xicaras cafes por dia':'2'
	,'Bis por dia':'17'
	,'Idade':'39'
	,'Peso':'122'
	,'Horas devidas':'25'
	,'Bananights por mes':'8'
	} ).save()

Buzz_user=User(name='Buzz', password='Buzz').save()

Buzz_card = Card( name='Buzz', attributes ={
	'Numero de commits no GitHub':'206'
	,'Tempo de jogo na Steam':'640'
	,'Xicaras cafes por dia':'3'
	,'Bis por dia':'3'
	,'Idade':'26'
	,'Peso':'74'
	,'Horas devidas':'45'
	,'Bananights por mes':'8'
	} ).save()

Sara_user=User(name='Sara', password='Sara').save()

Sara_card = Card( name='Sara', attributes ={
	'Numero de commits no GitHub':'293'
	,'Tempo de jogo na Steam':'796'
	,'Xicaras cafes por dia':'1'
	,'Bis por dia':'16'
	,'Idade':'22'
	,'Peso':'146'
	,'Horas devidas':'40'
	,'Bananights por mes':'4'
	} ).save()

Plato_user=User(name='Plato', password='Plato').save()

Plato_card = Card( name='Plato', attributes ={
	'Numero de commits no GitHub':'157'
	,'Tempo de jogo na Steam':'730'
	,'Xicaras cafes por dia':'6'
	,'Bis por dia':'0'
	,'Idade':'26'
	,'Peso':'76'
	,'Horas devidas':'74'
	,'Bananights por mes':'0'
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
