import re
namesRegex = re.compile(r'Agent (\w)\w*') #() grupe \1
mo = namesRegex.findall('Agent Alice gave the secrect document to Agent Bob.')
print(mo)

mo = namesRegex.sub(r'Agent \1****', 'Agent Alice gave the secrect document to Agent Bob.') # \1 grupe reiskia pirma vardo raide r' ; raw string
print(mo)


