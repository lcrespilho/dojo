import random

def init_nosql_patch( file ):
	file.write("from models import *\n\n")
	file.write("for user in User.nodes:\n")
	file.write("\tuser.delete()\n\n")
	file.write("for card in Card.nodes:\n")
	file.write("\tcard.delete()\n\n")
	file.write("for deck in Deck.nodes:\n")
	file.write("\tdeck.delete()\n\n")

def user_nosql_patch( file, translated ):
        file.write(translated[0]+"_user=User(name='"+translated[0]+"', password='"+translated[0]+"').save()\n\n")

def card_nosql_patch( file, translated ):
	file.write(translated[0]+"_card = Card( ")
	file.write("name='" + translated[0] +"', attributes ={\n")

	trans_size = len(translated)
	first = True
	for attr in range(1, trans_size, 2):
		cur_attr = str(translated[attr])
		value = str(translated[attr+1])
		if first:
			first = False
			file.write('\t')
		else:
			file.write('\t,')
		file.write("'"+cur_attr+"':'"+value+"'\n")
        file.write("\t} ).save()\n\n")

def deck_nosql_patch( file, translated ):
        
	deck_name = str(translated[0])+"_deck"
	file.write( deck_name +"= Deck( ")
	file.write("\nname='" + translated[0] +"', attributes = [\n")

	fields = translated[1].split(',')	
	fields_size = len(fields)
	first = True
	for attr in range(1, fields_size, 1):
		cur_attr = str(fields[attr])
		if first:
			first = False
			file.write('\t')
		else:
			file.write('\t,')
		file.write("'"+cur_attr+"'")
        file.write("\t] ).save()\n\n")

	trans_size = len(translated)
	first = True
	for attr in range(2, trans_size, 1):
		file.write(deck_name+".cards.connect("+str(translated[attr])+"_card)\n")

def translate_card( line ):
	translated = []

	current_line = line.split('|')
	line_size = len(current_line)
	translated.append(current_line[0])
	for attr in range(1, line_size, 2):
		translated.append(current_line[attr])
		translated.append(current_line[attr+1])

	return translated

def translate_deck( line ):
	return line.split('|')

def complete_attrs( translated, attrs, attrs_min, attrs_max ):
	random.seed()
	number_of_attrs = len(attrs)
	for curr in range(number_of_attrs):
		if not attrs[curr] in translated:
			min_value = int(attrs_min[curr])
			max_value = int(attrs_max[curr])
			random_value = random.randint(min_value, max_value)
			translated.append(attrs[curr])
			translated.append(random_value)







mocked_data = open('mocked.cards.py', 'w')

attr = []
attr_min = []
attr_max = []

base_card = open('base.cards', 'r')

for line in base_card:
	line = line.rstrip('\n')
	current_line = line.split('|')
	attr.append(current_line[0])
	attr_min.append(current_line[1])
	attr_max.append(current_line[2])


still_cards = True
mock_data = open('mock.cards', 'r')

init_nosql_patch( mocked_data )

for line in mock_data:
	line = line.rstrip('\n')
	if not line:
		continue
 	if line == "#cards":
		still_cards = True
		continue
 	if line == "#decks":
		still_cards = False
		continue
	if still_cards:
		translated = translate_card( line )
		complete_attrs( translated, attr, attr_min, attr_max )
		user_nosql_patch( mocked_data , translated )	
		card_nosql_patch( mocked_data , translated )	
	else:
		translated = translate_deck( line )
		deck_nosql_patch( mocked_data, translated );

