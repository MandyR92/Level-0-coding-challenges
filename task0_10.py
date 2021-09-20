def common_char(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    print("Common letter: ", end=" ")
    for letter in ('abcdefghijklmnopqrstuvwxyz'):
        if letter in string1 and letter in string2:
            print(letter, end=" ")
    

common_char("house", "computers")













