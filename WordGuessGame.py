import random
name = input("Enter your name: ")
print(f"Good Luck: {name}")
categories = {
    "Animals": [
        "tiger", "lion", "elephant", "giraffe", "zebra", "monkey",
        "kangaroo", "panda", "leopard", "cheetah", "rabbit", "deer",
        "wolf", "fox", "bear", "camel", "hippopotamus", "rhinoceros",
        "squirrel", "dolphin"
    ],

    "Fruits": [
        "apple", "banana", "mango", "orange", "grapes", "pineapple",
        "watermelon", "papaya", "guava", "kiwi", "peach", "pear",
        "strawberry", "blueberry", "raspberry", "pomegranate",
        "dragonfruit", "lychee", "apricot", "coconut"
    ],

    "Countries": [
        "india", "canada", "australia", "japan", "brazil", "germany",
        "france", "italy", "argentina", "mexico", "china", "russia",
        "egypt", "nepal", "bhutan", "norway", "sweden", "finland",
        "spain", "portugal"
    ],

    "Programming": [
        "python", "java", "javascript", "typescript", "kotlin",
        "variable", "function", "compiler", "algorithm", "database",
        "framework", "library", "backend", "frontend", "debugging",
        "inheritance", "polymorphism", "encapsulation", "recursion",
        "exception"
    ],

    "Sports": [
        "cricket", "football", "basketball", "volleyball", "tennis",
        "badminton", "hockey", "baseball", "rugby", "swimming",
        "cycling", "wrestling", "gymnastics", "archery", "kabaddi",
        "chess", "boxing", "golf", "snooker", "athletics"
    ],

    "Movies": [
        "inception", "avatar", "gladiator", "interstellar",
        "titanic", "joker", "frozen", "matrix", "rocky",
        "aladdin", "coco", "up", "gravity", "dunkirk",
        "skyfall", "memento", "casablanca", "godfather",
        "goodfellas", "whiplash"
    ],

    "Professions": [
        "doctor", "engineer", "teacher", "lawyer", "scientist",
        "architect", "pilot", "chef", "journalist", "accountant",
        "pharmacist", "dentist", "designer", "developer",
        "electrician", "mechanic", "surgeon", "veterinarian",
        "firefighter", "policeman"
    ],

    "Vehicles": [
        "car", "motorcycle", "bicycle", "airplane", "helicopter",
        "submarine", "scooter", "truck", "tractor", "bus",
        "ambulance", "spaceship", "train", "tram", "van",
        "yacht", "canoe", "ship", "rocket", "hovercraft"
    ],

    "Technology": [
        "computer", "keyboard", "monitor", "processor", "internet",
        "smartphone", "router", "bluetooth", "software", "hardware",
        "firewall", "server", "cloud", "artificialintelligence",
        "cybersecurity", "network", "microchip", "algorithm",
        "blockchain", "robotics"
    ],

    "Food": [
        "pizza", "burger", "sandwich", "biryani", "pasta",
        "noodles", "pancake", "omelette", "samosa", "dosa",
        "idli", "paratha", "cake", "chocolate", "icecream",
        "cookies", "lasagna", "soup", "salad", "tacos"
    ]
}
#words = ['rainbow', 'computer', 'science', 'programming','python', 'mathematics', 'player', 'condition','reverse', 'water', 'board', 'geeks']

c = 1
while c != 0:
    print("Choose from which Category you want to play the game:", end=" ")
    print(categories.keys())
    usr_inp = input().title()
    if usr_inp in categories.keys():
        word = random.choice(categories[usr_inp])
        c = 0
    else:
        continue


#word = random.choice(words)
#print(word)
print("Guess the Characters")
#for i in range(len(word)):
#    print("_",end = "")
guesses = ''
turns = 12
while turns > 0:
    failed = 0
    for ch in word:
        if ch in guesses:
            print(ch,end = " ")
        else:
            print("_", end = ' ')
            failed += 1
    print()
    if failed == 0:
        print("Congratulations you Won")
        print("The word is : ", word)
        break
    guess = input("Guess a character: ")
    if(len(guess) != 1):
        print("Please enter a single character")
        continue
    if guess in guesses:
        print("You had already guessed this character")
        continue
    guesses += guess
    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have ", + turns, " more guesses left")
        if turns == 0:
            print("You Lost the Game")
            print("The word was: ", word)

