from characterClass import Character

characters = { "a":Character("Garrosh"), "b":Character("Thrall"), "c":Character("Saurfang")}
alive_characters = len(characters)

while alive_characters > 1:

    print
    for character_name in sorted(characters.keys()):
        print character_name, characters[character_name]
    first = raw_input("Who attacks? ").lower()
    second = raw_input("Who is the target? ").lower()

    try:
        first_character = characters[first]
        second_character = characters[second]
    except KeyError, name:
        print ("*" * 30)
        print ("No such character!", name)
        print ("*" * 30)
        continue

    if not first_character.alive or not second_character.alive:
        print ("*" * 30)
        print "One of those people is dead!"
        print ("*" * 30)
        continue
    print
    print ("*" * 30)

    first_character.fire_at(second_character)
    if not second_character.alive:
        alive_characters -=1
    print ("*" * 30)

for character in characters.values():
    if character.alive:
        print (character.name, "is the winner!")
        break
