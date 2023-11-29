import time

def introduction():
    print("Welcome to the Disney Adventure!")
    print("Embark on a magical journey with your favorite Disney characters.")

def make_choice(question, options):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def lion_king_story():
    print("\nYou find yourself in the vast Pride Lands, where the circle of life unfolds.")
    time.sleep(1)
    print("The sun is setting, and Simba, the young lion cub, awaits your decision.")
    choice = make_choice("What will you do?", ["Join Simba on a journey", "Visit Rafiki's tree", "Explore the Elephant Graveyard"])

    if choice == 1:
        print("\nSimba's eyes light up as you decide to join him on a journey.")
        time.sleep(1)
        print("Together, you face challenges, overcome Scar's tyranny, and restore balance to the Pride Lands.")
        return "happy_ending"
    elif choice == 2:
        print("\nYou decide to visit Rafiki's tree, seeking guidance from the wise mandrill.")
        time.sleep(1)
        print("Rafiki shares the importance of embracing your true identity, and you leave with newfound purpose.")
        return "happy_ending"
    else:
        print("\nCuriosity leads you to the Elephant Graveyard, a place filled with danger.")
        time.sleep(1)
        print("Though you narrowly escape peril, the experience grants you courage and resilience.")
        return "neutral_ending"

def frozen_story():
    print("\nYou enter the enchanting kingdom of Arendelle, where an icy tale awaits.")
    time.sleep(1)
    print("Elsa, the Snow Queen, and her sister Anna are at the heart of the story.")
    choice = make_choice("What will you do?", ["Help Elsa control her powers", "Visit Olaf in the enchanted forest", "Confront Prince Hans"])

    if choice == 1:
        print("\nDetermined to help Elsa, you join forces to control her magical abilities.")
        time.sleep(1)
        print("Arendelle thrives, and Elsa learns the power of love and self-acceptance.")
        return "happy_ending"
    elif choice == 2:
        print("\nIn the enchanted forest, you encounter Olaf, the friendly snowman, and his enchanted tales.")
        time.sleep(1)
        print("While the forest is filled with wonders, you leave with a heart touched by magic.")
        return "neutral_ending"
    else:
        print("\nConfronting Prince Hans reveals a treacherous plot against Arendelle.")
        time.sleep(1)
        print("Through bravery and teamwork, you thwart Hans' plans, ensuring the kingdom's safety.")
        return "happy_ending"

def play_game():
    introduction()

    initial_choice = make_choice("Choose a Disney story to explore:", ["The Lion King", "Frozen"])

    if initial_choice == 1:
        ending = lion_king_story()
    else:
        ending = frozen_story()

    print("\nYour Disney adventure concludes.")
    print(f"You reached the {ending}.")

if __name__ == "__main__":
    play_game()