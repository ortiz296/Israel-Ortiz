def pluralize(word):
    if word[-3:] == "ife":
        return(word[:-3] + "ives")
    elif word[-2:] == "ch" or word[-2:] == "sh":
        return(word + "es")
    elif word[-2:] == "us":
        return(word[:-2] + "i")
    elif word[-2:]=="ay" or word[-2:]=="oy" or word[-2:]=="ey" or word[-2:]=="uy":
        return(word + "s")
    elif( word[-1:]=="y"):
        return(word[:-1] + "ies")
    else:
        return word + 's'

word=raw_input("enter a word: ")
print pluralize(word)
