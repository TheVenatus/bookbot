def word_counter(text):
    return len(text.split())

def number_letter(text):
    counter = 0
    counts = {}
    single_letter = set()
    ltext = text.lower()
    for lletter in ltext:
        single_letter.add(lletter)
    for letter in single_letter:
        number = ltext.count(letter)
        counts[letter] = number
    return counts

def myFunc(e):
    return e["num"]

def sort(counts):
    new_list = []
    liste_von_tupeln = list(counts.items())
    for tupel in liste_von_tupeln:
       letter, count = tupel
       if letter.isalpha():
        dictionary = {}
        dictionary["char"] = letter
        dictionary["num"] = count
        new_list.append(dictionary)
    new_list.sort(reverse=True, key=myFunc)
    return new_list