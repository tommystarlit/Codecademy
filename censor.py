def censor(word):
    for i in word:
        word(i) = "*"
    return word

censor("abanana")

