#! python3

import re, pyperclip

# Create a regex for phone numbers
pnoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(

((\d\d\d)|(\(\d\d\d))?         # area code (optional)

(\s|-|\d{0,9})  # first separator
\d\d\d  # first 3 digits
(-|\.)           # separator
\d\d\d\d            # last 4 digits
(((ext(\.)?\s)|x)           #extension word part(optional)
 (\d{2,5}))?          # extension number-part (optional)

)
''', re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile(r'''
# some.+_thing@something.com

[a-zA-Z0-9_.+]+        # name part
@                       # @ symbol
[a-zA-Z0-9_.+]+        # domain name part

''', re.VERBOSE)
# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email phone from this text
extractedPhone = pnoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])


# Copy the extracted email phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
