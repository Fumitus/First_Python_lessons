from random import choice
questions = ["Kas čia?: ",
             "Kada atvažiuosim???: ",
             "Galima ir man?: ",
             "Kodėl dangus mėlynas?: ",
             "Kodėl mėnulis turi veidą?: "]

question = choice(questions)
answer = input(question).strip().lower()

while answer !="todėl":
    answer = input("Kodėl? ").strip().lower()
print("Gerai....")

