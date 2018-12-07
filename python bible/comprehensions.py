even_numbers = [x for x in range(1, 101) if x%2 == 0]
print(even_numbers)

odd_numbers = [x for x in range(1, 101) if x%2 != 0]
print(odd_numbers)



#kitas pavyzdys

words = ["enter", "the", "correct", "Sentence"]
answer = [[w.upper(), w.lower(), len(w)] for w in words]
print(answer)

