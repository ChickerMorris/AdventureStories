#chat adventure
#author Zachary Morris
import time

choice1 = [
	"Look Around",
	"Light the Room"
]

choice2 = [
	"Torch",
	"Campfire"
]

choice3 = [
	"Go out the door",
	"Stay and wait"
]

choice2_1 = [
	"Go back",
	"Gather Sticks"
]

choice2_2 = [
	"Help the girl and go back",
	"Leave her there"
]

choice2_3 = [
	"help her",
	"Don't help her"
]

choice3_1 = [
	"tower",
	"cabin",
	"trapdoor"
]

choice3_2 = [
	"push her off",
	"don't push her off"
]

choice3_3 = [
	"you jump down",
	"the girl jumps down"
]

light = 0
sticks = 0
lvl = 1
ending = 0

print("Hello and welcome to the tower")
time.sleep(1)
name = raw_input("---What is your name?, this will determine everything in the game---")
print("shall we begin? (remember this game is case sensitive)")
time.sleep(2)

print("You wake up in a dark room not a bit of light in site")

#the beginning of the choices
while True:
	#lvl1 the dark room
	print(choice1)
	answ1 = raw_input("---what do you do?---")
	#the 1st tree, 1st level
	if answ1 == "stop":
		break
	if answ1 == "Look Around":
		print("*you cannot see anything, except for a stick in front of you*")
	elif answ1 == "Light the Room":
		print(choice2)
		anws1_2 = raw_input("---What do you make?---")
		if anws1_2 == "Torch":
			print("you pick up the stick in front of you and strike it against the ground, you just barely are able to make it light")
			light += 1
			print("*You can now see the room*")
		if anws1_2 == "Campfire":
			print("You need sticks")
			if sticks == 1:
				print("you make a Campfire and get warm near by it, it is a feeling you have never felt before you decide to stay there, forever")
			elif sticks == 1:
				while True:
					print("You starve")
	else:
		print("I am sorry?")

	#the 2nd tree, 1st level
	if answ1 == "Look Around" and light == 1:
		print("you look around the room, you see brick walls and a door")
		print(choice3)
		answ2 = raw_input("---What will you do?---")
		if answ2 == "stop":
			break
		if answ2 == "Go out the door":
			print("you see a blinding light in front of you")
			lvl += 1
		elif answ2 == raw_input("Stay and wait"):
			print("you decided to wait for someone to come and find you")
			time.sleep(1)
			print("No one came, and no one ever will, no matter how long you wait they will never come never. You starve")
	while True and lvl == 2:
		#Lvl2 The forest, 1st tree
		print("*****")
		print("the blinding light slowly turns into a forest, a strangly silent and foggy forest")
		print(choice2_1)
		answ3 = raw_input("---What will you do?---")
		if answ3 == "Gather Sticks":
			print("you go out to find sticks")
			sticks += 1
			print("You find a girl passed out on the ground")
			print(choice2_2)
			answ4 = raw_input("---What will you do?---")
			#2nd tree, 2nd Level
			if answ4 == "Help the girl and go back":
				print("you pick up the girl and go back to the room with her")
				time.sleep(1)
				print("she wakes up and tells you that she woke up strangly here to.")
				print(choice2_3)
				answ5 = raw_input("---Will you help her?---")
				if answ5 == "help her":
					print("you decide to help her and so you set out to find why you guys were here")
					lvl += 1
				elif answ5 == "Don't help her":
					print("you feel a blunt object hit your head as everything goes black")
				else:
					print("what?")
			elif answ4 == "Leave her there":
				print("you decide to leave here there and head back to the house")
				if sticks == 1:
					print("You head back to the house and make a campfire, you stay there. forever")
		elif answ3 == "Go back":
			print("You decide to go back into the house. It is lonely in the house. You stay. Forever")
		else:
			print("I am Sorry?")
			time.sleep(1)
		while True and lvl == 3:
			#1st tree, final level
			print("*****")
			print("After hours of searching in the fog you find three things")
			print(choice3_1)
			answ6 = raw_input("---Where will you go?---")
			#this keeps the player from going back to a place they were before
			if answ6 == "tower" and ending >= 1:
				print("something tells you not to go there")
			elif answ6 == "cabin" and ending >= 1:
				print("something tells you not to go there")
			elif answ6 == "trapdoor" and ending >= 1:
				print("something tells you not to go there")
			#the end of the game
			if answ6 == "tower":
				print("you decide to head out and search the tower")
				time.sleep(2)
				print("you went to the top of the tower and found nothing, a fall from this height could kill someone")
				print("----------")
				print(choice3_2)
				answ7 = raw_input("Will you...?")
				if answ7 == "push her off":
					print("you pushed the girl off, you never really even liked her you only helped her because you thought she would be a good girlfriend, when you finally went back down the tower, you black out and then never see the light of day again.")
					ending += 1
				elif answ7 == "don't push her off":
					print("You don't push her off and walk all the way down the tower")
					ending += 1
			elif answ6 == "cabin":
				print("you decide to go to the abandoned cabin with the girl. Years flew by as you and her grew old together and made a famiily for the next generation")
				ending += 1
			elif answ6 == "trapdoor":
				print("you both head out to the trapdoor and open it, it is too dark to see")
				print(choice3_3)
				answ8 = raw_input("one of you needs to jump down there, who?")
				if answ8 == "you jump down":
					print("you jump down into the dark pit below, smoething breaks your fall, it feels. human. Above you, you see the girl close the trapdoor above you. leaving you to stay down in the pit below.")
					ending += 1
				elif answ8 == "the girl jumps down":
					print("you both decide that she should go down into the depths below. as she jumps she grabs your arm, taking you both down into the depts below...")
					ending += 1
			else:
				print("you looked around and could not find that")
			if ending == 3:
				time.sleep(3)
				print("*************************************")
				print("sometimes life doesn't have happy endings, sometime life will lead you into a dark pit below or you will regret a decision that you made one moment ago. Or sometimes, you are able to find peace and love throughout it all, but when it comes to end of things. it just doesn't matter. it. just. doesn't. matter.")
				break

