name = input('Enter your name please: ').strip()
age = int(input('Please enter your age: '))
if name == 'Alice':
    print('Hi Alice')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age >2000:
    print('Unlike you, Alice is not an undead, imortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')
    
