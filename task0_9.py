def display_vowels(word):
    lst = []
    word = word.lower()
    print("vowels: ", end=" ")
    for vowel in "aeiou":
        if vowel in word:
            x = lst.append(vowel)
    for vowel in lst:
        if vowel == lst[-1]:
            print(vowel)
        else:
            print(vowel + ", ", end="")
    


display_vowels("Umuzi")


