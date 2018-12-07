#get user email address

email = input("What is your email adress?: ").strip()

#slice out user name

user = email[:email.index("@")]

#slice domain name

domain = email[email.index("@") + 1 :]

#display output message

output = "Your username is {} and your domain name is {}".format(user, domain)
print(output)
