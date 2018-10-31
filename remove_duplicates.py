def remove_duplicates(lst):
  out = []
  for i in range(len(lst)):
    if lst[i] not in out:
      out.append(lst[i])
  return out