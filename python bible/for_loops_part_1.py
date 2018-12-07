balsiai = 0
priebalsiai = 0
word = input("Įveskite žodį garsų analizei?: ").strip().lower()

for letter in word:
        if letter.lower() in "aeiou":
            balsiai = balsiai + 1
        elif letter ==" ":
            pass
        else:
           priebalsiai = priebalsiai + 1
print("žodyje yra {} balsiai".format(balsiai))
print("žodyje yra {} priebalsiai".format(priebalsiai))

