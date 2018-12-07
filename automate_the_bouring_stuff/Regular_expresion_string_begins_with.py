import re

beginsWithHelloRegex = re.compile(r'^Hello')
mo = beginsWithHelloRegex.search('Hello there!') # Hello eilut4s prad=ioje. Tenkinama salyga
print(mo)

beginsWithHelloRegex = re.compile(r'^Hello')
mo = beginsWithHelloRegex.search('He said "Hello!"') # Hello sakinio gale. salyga netenkinama
print(mo)

endsWithWordRegex = re.compile(r'world!$') #True world! sakinio gale
mo = endsWithWordRegex.search('Hello world!')
print(mo)

endsWithWordRegex = re.compile(r'world!$')
mo = endsWithWordRegex.search('Hello world! are anybody here') #None 
print(mo)


allDigitsRegex = re.compile(r'^\d+$')
mo = allDigitsRegex.search('dhfdh 1254872 dthfhedhjj')
print(mo)

atRegex = re.compile(r'.at')
mo = atRegex.findall('The cat in the hat sat on the flat mat.') #. rei6kia bet kuris simbolis išskyrus naują eilutę
print(mo)

atRegex = re.compile(r'.{1,2}at')
mo = atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo)


name = 'First Name: Al Last Name: Sweigart'
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.findall(name)
print(mo)


naujaEilute = '''First Name: Al
Last Name: Sweigart'''

nameRegex = re.compile(r'First Name: (.*)\nLast Name: (.*)')
mo = nameRegex.findall(naujaEilute)
print(mo)



serve = '<To serve humans> for dinner.>'
nongreedy = re.compile(r'<(.*?)>') #?
mo = nongreedy.findall(serve)
print(mo)

serve = '<To serve humans> for dinner.>'
nongreedy = re.compile(r'<(.*)>') # n4ra ? simbolio
mo = nongreedy.findall(serve)
print(mo)

prime = 'Serve the public trust.\nProtect the innocnent.\nUpload the law.'
dotStar = re.compile(r'.*') # . reiškia bet koks simbolis išskyrus naują eilutę \n
mo = dotStar.search(prime)
print(mo)

prime = 'Serve the public trust.\nProtect the innocnent.\nUpload the law.'
dotStar = re.compile(r'.*', re.DOTALL) # re.DOTALL . jau reiškia Visi6kai Viską
mo = dotStar.search(prime)
print(mo)

text = 'Al, why does your programming book talk about RoboCop so much?'
vowelRegex = re.compile(r'[aeiou]')
mo = vowelRegex.findall(text)
print(mo)

text = 'Al, why does your programming book talk about RoboCop so much?'
vowelRegex = re.compile(r'[aeiou]', re.I) #i reiskia IGNORECASE 5traukia ir Didziasias ir mazasias balses
mo = vowelRegex.findall(text)
print(mo)
