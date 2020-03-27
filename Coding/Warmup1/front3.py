def front3(str):
  pref = 3
  if len(str) < pref:
    pref = len(str)
  copy = str[:pref]
  return copy + copy + copy 