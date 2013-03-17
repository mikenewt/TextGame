# item inventory
items = []

# prints the error message and returns user to room func
def error(func):
	print "I'm sorry but I don't know what you mean."
	func()

# start in the garden
def the_garden():
	print "The golden glow of the setting afternoon sun cuts through your eyelids as it dips below the branches of the tree you were sleeping under."
	print "You recall that you fell asleep in the courtyard garden of this aging castle. An urgent nagging in your stomach tells you that you must be forgetting something important."
	print "A rumble like boulders falling from mountains shakes the foundations of the castle. It appears to have come from the highest tower in the castle."
	print "Exits: North, East, South"

	next = raw_input("> ")

	if next == "north" or next == "n":
		the_library()
	elif next == "south" or next == "s":
		the_bedroom()
	elif next == "east" or next == "e":
		the_stairs()
	else:
		error(the_garden)

# go north to library
def the_library():
	print "The years have not been kind to this library. Dust lies heavy on toppled bookcases and the ancient tomes spilled all over the floor."
	print "Nearby, a table with three large books sits undisturbed among the chaos."
	print "Exits: South"

	next = raw_input("> ")

	if next == "south" or next == "s":
		the_garden()
	elif next == "get book":
		print "You pick up the book. It rattles strangely as though something were loose inside."

		book = raw_input("> ")

		# add key to items, used in the_bedroom
		if book == "open book":
			print "A key falls out of the inside of the book and onto the table. You put it in your pocket and leave the library."
			items.append("key")
			the_garden()
		else:
			error(the_library)

	else:
		error(the_library)

#go south to bedroom
def the_bedroom():
	print "Pieces of broken porcelain and shattered furniture crunch underfoot as you make your way south into the master bedroom."
	print "The ravages of time have turned the formerly opulent bedroom into a mess of rotting linen and cobwebs."
	print "In the corner of the room a heavily scarred chest sits stubbornly intact among the surrounding ruins."
	print "Exits: North"

	next = raw_input("> ")

	# get sword used against dragon in the_tower, remove key from items[]
	if next == "open chest":
		if items == []:
			print "That is locked. Perhaps you should look for the key?"
			the_bedroom()
		else:
			print "You insert the key into the lock and turn it slowly. Pop! The lock clicks and the lid swings open."
			print "Inside the chest is a beautiful sword with a shining golden hilt. You gently lift it out of the chest and return to the garden."
			items.remove("key")
			items.append("sword")
			the_garden()
	elif next == "north" or next == "n":
		the_garden()
	else:
		error(the_bedroom)

# go east to the stairs
def the_stairs():
	print "Under construction."


	

the_garden()