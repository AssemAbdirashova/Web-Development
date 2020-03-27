def last2(str):
  if len(str) < 2:
    return 0
  count = 0
  last_two_chars = str[len(str)-2:]
   
  for i in range(len(str)-2):
    sub = str[i:i+2]
    if sub == last_two_chars:
      count += 1

  return count