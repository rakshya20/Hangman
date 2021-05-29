def anagram(word):
    second_word = word[::-1]
    if word == second_word:
        print("It is anagram") 
    else: 
        print('It is not anagram')

anagram('madam')