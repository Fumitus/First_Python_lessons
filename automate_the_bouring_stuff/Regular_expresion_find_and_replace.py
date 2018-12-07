import re
namesRegex = re.compile(r'Agent \w+')
mo = namesRegex.findall('Agent Alice gave the secrect document to Agent Bob.')
print(mo)

mo = namesRegex.sub('REDACTED', 'Agent Alice gave the secrect document to Agent Bob.')
print(mo)

namesRegex = re.compile(r'Agent (\w)\w*')
mo = namesRegex.findall('REDACTED', 'Agent Alice gave the secrect document to Agent Bob.')
print(mo)
