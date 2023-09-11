import random

roll = ''
response = input("Do you want to roll a dice y or n: ")

if response == "y":
    roll = input("Press y to roll or press n to exit: ")
    while roll != "n":
        random_number = random.randint(1,6)
        if random_number == 1:
            print("[-----]")
            print("[     ]")
            print("[  o  ]")
            print("[     ]")
            print("[-----]")

        if random_number == 2:
            print("[-----]")
            print("[    o]")
            print("[     ]")
            print("[o    ]")
            print("[-----]")

        if random_number == 3:
            print("[-----]")
            print("[    o]")
            print("[  o  ]")
            print("[o    ]")
            print("[-----]")

        if random_number == 4:
            print("[-----]")
            print("[o   o]")
            print("[     ]")
            print("[o   o]")
            print("[-----]")

        if random_number == 5:
            print("[-----]")
            print("[o   o]")
            print("[  o  ]")
            print("[o   o]")
            print("[-----]")

        if random_number == 6:
            print("[-----]")
            print("[o   o]")
            print("[o   o]")
            print("[o   o]")
            print("[-----]")

        roll = input("Press y to roll or press n to exit: ")
        
print("BYE")