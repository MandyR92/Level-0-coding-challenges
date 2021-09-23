def common_char(string1, string2):
    lst = []
    string1 = string1.lower()
    string2 = string2.lower()
    print("'Common letters:", end="")
    for letter in ('abcdefghijklmnopqrstuvwxyz'):
        if letter in string1 and letter in string2:
            x = lst.append(letter)
    for letter in lst:
        if letter == lst[-1]:
            print(letter + "'")
        else:
            print(letter + ",", end="")
    

common_char("house", "computers")



