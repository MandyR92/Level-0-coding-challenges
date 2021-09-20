def display_vowels(word):
    word = word.lower()
    print("vowels:", end=" ")
    for vowel in "aeiou":
        if vowel in word:
            print(vowel, end=" ")


display_vowels("Umuzi")
