def count(sequence, item):
  counter = 0
  for i in range(len(sequence)):
    if sequence[i] == item:
      counter+=1
  return counter
