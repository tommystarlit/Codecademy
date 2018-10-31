def censor(text, word):
  list = text.split()
  for i in range(len(list)):
    if list[i] == word:
      list[i] = "*"*len(list[i])
  censor = " ".join(list)
  return censor

