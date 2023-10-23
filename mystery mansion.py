def mystery_mansion_combined():
    print("Welcome to the Mystery Mansion!")
    print("You find yourself standing in front of an old, spooky mansion.")
    
    has_key = False
    has_map = False
    has_flashlight = False
    
    while True:
        print("\nWhat do you want to do?")
        print("1. Enter the mansion")
        print("2. Walk around the garden")
        print("3. Knock on the door")
        print("4. Check the mailbox")
        print("5. Leave")
        
        choice = input("Enter your choice (1/2/3/4/5): ")
        
        if choice == '1':
            print("You enter the mansion and hear a creaking sound coming from the basement.")
            basement_choice = input("Do you want to investigate the basement? (yes/no): ").lower()
            if basement_choice == 'yes':
                print("You head down to the basement and find a dusty library.")
                library_choice = input("Do you want to read a book or continue exploring? (book/exploring): ").lower()
                if library_choice == 'book':
                    print("You find an interesting book that contains a cryptic riddle.")
                else:
                    print("You continue exploring the mansion.")
                if has_flashlight:
                    print("You use the flashlight to explore the dark hallway and find a hidden room.")
                    print("Inside, you discover a chest with a valuable treasure.")
                    print("Congratulations, you win!")
                    break
            else:
                print("You decide not to go to the basement and continue exploring the mansion.")
        
        elif choice == '2':
            print("You explore the garden and find a key hidden under a pile of leaves.")
            has_key = True
            print("You can use this key to enter the mansion.")
            garden_choice = input("Where do you want to go now? (mansion/leave): ").lower()
            if garden_choice == 'mansion':
                print("You unlock the mansion door with the key and enter the foyer.")
                if has_map:
                    print("You use the map to navigate to the secret room.")
                    print("Inside, you find a valuable artifact.")
                    print("Congratulations, you win!")
                    break
            else:
                print("You decide to leave the area.")
        
        elif choice == '3':
            print("You knock on the door, but there's no answer. It's as if the mansion is abandoned.")
            door_choice = input("What do you want to do next? (1/2/4/5): ").lower()
            if door_choice == '1':
                print("You enter the mansion.")
                if has_flashlight:
                    print("You use the flashlight to explore the dark hallway and find a hidden room.")
                    print("Inside, you discover a chest with a valuable treasure.")
                    print("Congratulations, you win!")
                    break
            elif door_choice == '2':
                print("You decide to explore the garden.")
            elif door_choice == '4':
                print("You check the mailbox and find a mysterious letter with a riddle.")
                riddle_answer = input("Can you solve the riddle? (yes/no): ").lower()
                if riddle_answer == 'yes':
                    print("You solve the riddle and find a hidden key.")
                    has_key = True
                else:
                    print("The riddle remains unsolved.")
            elif door_choice == '5':
                print("You decide to leave the area.")
        
        elif choice == '4':
            print("You decide to check the mailbox and find a mysterious letter with a riddle.")
            riddle_answer = input("Can you solve the riddle? (yes/no): ").lower()
            if riddle_answer == 'yes':
                print("You solve the riddle and find a hidden key.")
                has_key = True
            else:
                print("The riddle remains unsolved.")
        
        elif choice == '5':
            print("You decide to leave the mansion.")
            print("Thanks for playing!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    mystery_mansion_combined()
