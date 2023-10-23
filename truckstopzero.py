import time

# Define a class for the player character
class Player:
    def __init__(self):
        self.name = "Player"
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)

# Define a class for non-player characters (NPCs)
class NPC:
    def __init__(self, name, description):
        self.name = name
        self.description = description

# Define a class for locations/rooms
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
        self.items = []
        self.characters = []

    def add_paths(self, paths):
        self.paths.update(paths)

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

# Define a class for puzzles
class Puzzle:
    def __init__(self, description, solved=False):
        self.description = description
        self.solved = solved

    def solve(self):
        self.solved = True

# Define a class for quests
class Quest:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def complete(self):
        self.completed = True

# Create game rooms
start = Room("Start", "You find yourself in a forest. There is a path to the north.")
cave = Room("Cave", "You enter a dark cave. There is a key on the ground.")
river = Room("River", "You arrive at a fast-flowing river. There is a boat on the shore.")
bridge = Room("Bridge", "You cross a bridge and reach a small cabin. It is locked.")
cabin = Room("Cabin", "You enter the cabin. A mysterious figure is sitting in the corner.")

clearing = Room("Clearing", "You stand in a small clearing. There is a well in the center.")
well = Room("Well", "You approach the well. It's dark and deep. You hear faint whispers coming from within.")
cave_exit = Room("Cave Exit", "You find yourself at the exit of the cave. Sunlight pours in from outside.")
forest = Room("Forest", "You are in a dense forest. There is an abandoned campsite here.")
secret_chamber = Room("Secret Chamber", "You've discovered a hidden chamber deep within the cave.")
campsite = Room("Campsite", "You arrive at an abandoned campsite. The fire is still smoldering.")
village = Room("Village", "You enter a peaceful village, with friendly villagers going about their business.")

# Create game items
key = "Key"
boat = "Boat"
flashlight = "Flashlight"
note = "Note"
worn_map = "Worn Map"
lantern = "Lantern"
treasure_map = "Treasure Map"
ancient_amulet = "Ancient Amulet"

# Create characters
mysterious_figure = NPC("Mysterious Figure", "A hooded figure sits in the corner, observing you.")
villager = NPC("Villager", "Hello, traveler! Welcome to our village. We are known for our legendary treasure.")

# Create puzzles
cabin_puzzle = Puzzle("The cabin door is locked. You need to find a key to unlock it.")
campfire_puzzle = Puzzle("The campfire is smoldering, but you need to get it going to find the treasure.")
treasure_puzzle = Puzzle("You've found the treasure chest, but it's locked. You need to find the key.")

# Create quests
find_flashlight = Quest("Find a flashlight to explore the well.")
find_treasure = Quest("Find the hidden treasure in the cave.")

# Add room connections
start.add_paths({"north": cave})
cave.add_paths({"south": start, "east": river})
river.add_paths({"west": cave, "swim": bridge})
bridge.add_paths({"enter": cabin})
cabin.add_paths({"exit": bridge})

cave_exit.add_paths({"south": secret_chamber})
secret_chamber.add_paths({"north": cave_exit, "west": campsite})
campsite.add_paths({"east": secret_chamber, "north": village})
village.add_paths({"south": campsite})

# Add items to rooms
cave.add_item(key)
cave.add_item(note)
forest.add_item(worn_map)
campsite.add_item(lantern)
secret_chamber.add_item(treasure_map)
village.add_item(ancient_amulet)

# Initialize game state
current_room = start

# Main game loop
while True:
    print("\n" + current_room.name)
    print(current_room.description)

    if current_room.items:
        print("You see the following items in the room:", ", ".join(current_room.items))

    if current_room.characters:
        print("You see the following characters in the room:", ", ".join([character.name for character in current_room.characters]))

    action = input("What do you want to do? ").lower()

    if action == "quit":
        break
    elif action == "inventory":
        print("Inventory:", ", ".join(player.inventory) if player.inventory else "Your inventory is empty.")
    elif action == "look around":
        print(current_room.description)
    elif action == "solve puzzle":
        if current_room == bridge and not cabin_puzzle.solved:
            print("You need to unlock the cabin door first.")
        elif current_room == bridge and key in player.inventory:
            cabin_puzzle.solve()
            print("You unlock the cabin door.")
        elif current_room == well and not find_flashlight.completed:
            print("It's too dark to explore. You need a light source.")
        elif current_room == campsite and not campfire_puzzle.solved:
            print("The campfire is smoldering. You need to get it going to find the treasure.")
        elif current_room == secret_chamber and not find_treasure.completed:
            print("You've found the treasure chest, but it's locked. You need to find the key.")
        else:
            print("There are no puzzles to solve here.")
    elif action == "take":
        if current_room.items:
            item = input("What item do you want to take? ").capitalize()
            if item in current_room.items:
                player.add_item(item)
                current_room.remove_item(item)
                print(f"You took the {item}.")
                if item == flashlight:
                    find_flashlight.complete()
                elif item == ancient_amulet:
                    find_treasure.complete()
            else:
                print("That item is not here.")
        else:
            print("There are no items in the room to take.")
    elif action == "drop":
        if player.inventory:
            item = input("What item do you want to drop? ").capitalize()
            if item in player.inventory:
                player.remove_item(item)
                current_room.add_item(item)
                print(f"You dropped the {item}.")
            else:
                print("You don't have that item in your inventory.")
        else:
            print("Your inventory is empty.")
    elif action == "talk":
        if current_room == cabin:
            print(f"{mysterious_figure.name}: Welcome, {player.name}. You are the chosen one.")
        elif current_room == village:
            print(f"{villager.name}: Traveler, we have a legend of hidden treasure in the cave.")
    elif action == "examine well" and current_room == well and find_flashlight.completed:
        current_room = cave
    elif action == "examine campfire" and current_room == campsite and lantern in player.inventory:
        campfire_puzzle.solve()
        print("You light the campfire, revealing a hidden tunnel.")
    elif action == "examine treasure chest" and current_room == secret_chamber and treasure_puzzle.solved:
        print("You open the treasure chest and find a precious ancient amulet!")
        player.add_item(ancient_amulet)
    elif action in current_room.paths:
        current_room = current_room.paths[action]
    else:
        print("Invalid action. Try something else.")

print("Thanks for playing!")
