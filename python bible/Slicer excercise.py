# here is a very long word

word = "antidisestablishmentarianism"

# use a slice to take out the word "establishment"
# and store it in the answer variable....
answer = word[word.index("establishment"):word.index("arian"):1]

print(answer)
