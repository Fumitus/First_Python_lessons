known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]

while True:
    print("Hi! Mano vardas Travis")
    name = input("Kuo tu vardu?: ").strip().capitalize()

    if name in known_users:
        
        print("Labas {}!".format(name))
        remove = input("Ar norėtum, kad ištrinčiau tave iš sąrašo (y/n)?: ").strip().lower()

        if remove == "y":
            known_users.remove(name)
        elif remove == "n":
            print("Gerai, vistiek norėjau tave palikti sąraše!")

    else:
        
        print("Nesu tavęs sutikęs {}".format(name))
        add_me = input("Ar norėtum, kad įtraukčiau tave į svečių sąrašą (y/n)?: ").strip().lower()
        if add_me == "y":
            known_users.append(name)
        elif add_me == "n":
            print("Iki kito karto!")
        
        
