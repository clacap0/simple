"""
Count the vowels in a string
"""

def count_vowels(phrase):
    vowels = 'aeiou'
    counter = 0
    for letter in phrase:
        for vowel in vowels:
            if vowel==letter:
                counter += 1

    return f'There are {counter} vowel(s) in your phrase.'

print(count_vowels(input('What phrase would you like to input? ').lower()))