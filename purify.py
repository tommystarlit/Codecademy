def purify(lst):
  pure = []
  for i in range(len(lst)):
    if lst[i]%2 == 0:
      pure.append(lst[i])
  return pure