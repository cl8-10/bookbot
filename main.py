

def count_words(txt):
    words = txt.split()
    count = len(words)
    return count

def count_letters(txt):
    cars = {}
    for i in txt:
        j = i.lower()
        if j not in cars:
            cars[j] = 1
        else:
            cars[j] += 1
    return cars

def sort_it(characters):
    lets = []
    for i in characters:
        if i.isalpha():
            lets.append(i)
    lets.sort()
    return lets

def report(wrd, chars, letters):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"Frankenstein contains {wrd} words")
    print()
    for l in letters:
        print(f"The letter {l} appears {chars[l]} times")

with open("books/frankenstein.txt") as f:

    file_contents = f.read()
    total_words = count_words(file_contents)
    characters = count_letters(file_contents)
    letts = sort_it(characters)
    report(total_words, characters, letts)


