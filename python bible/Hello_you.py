# Ask user for name

name = input("What is your name?: ")

#Ask user for age

age = input("How old are you?: ")

#Ask user where he lives

place = input("Where do you live?: ")

#Ask user how he is doing

mood = input("Are you happy?: ")


#Create output text

string = "Your name is {} and you are {} years old. You live in {} and you are happy? {}"
output = string.format(name, age, place, mood)

#Print output to screen
print(output)
