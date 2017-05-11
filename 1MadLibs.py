"""This is a game of MadLibs. It will take the user's input and add it to out MadLibs story. ENJOY!"""

print "Let's get started with a gme of Mad Libs!!"

main_character = raw_input("What the name of your character? ")
adjective1 = raw_input("Give me an adjective: ")
adjective2 = raw_input("Give me an adjective: ")
adjective3 = raw_input("Give me an adjective: ")
verb1 = raw_input("Give me a verb: ")
verb2 = raw_input("Give me a verb: ")
verb3 = raw_input("Give me a verb: ")
noun1 = raw_input("Give me a noun: ")
noun2 = raw_input("Give me a noun: ")
noun3 = raw_input("Give me a noun: ")
noun4 = raw_input("Give me a noun: ")
animal = raw_input("Give me an animal: ")
food = raw_input("Give me a food: ")
fruit = raw_input("Give me a fruit: ")
number = raw_input("Give me a number: ")
superhero = raw_input("Give me a superhero name: ")
country = raw_input("Give me a country: ")
dessert = raw_input("Give me a dessert: ")
year = raw_input("Give me a year: ")



#The template for the story
STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to the rythym of the %s, which made all of the %ss very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %ss ruled the world." % (adjective1,main_character,verb1,adjective2,noun1,noun2,animal,food,verb2,noun3,fruit,adjective3,superhero,verb3,number,main_character,superhero,superhero,main_character,country,main_character,dessert,main_character,year,noun4)

print STORY
