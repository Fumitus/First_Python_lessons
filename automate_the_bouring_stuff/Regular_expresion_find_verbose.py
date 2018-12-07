import re

phoneNumRegex = re.compile(r'''
(\d\d\d)|     # area code (without parens, with dash)
(\(\d\d\d\) ) # -or- area code with parens and no dash
\d\d\d        # first 3 digits
-             #second dash
\d\d\d\d      # last 4 digits
\sx\d{2,4}    # extension, like x1234''', re.IGNORECASE | re.DOTALL | re.VERBOSE) #re.IGNORECASE | re.DOTALL | re.VERBOSE gali but naudojamos bet kada
mo = phoneNumRegex.findall('555-222-2548,255-5544')
print(mo)
