def end_other(a, b):
  str1, str2 = (a,b) if len(a) >= len(b) else (b,a)
  return str1.lower().endswith(str2.lower())