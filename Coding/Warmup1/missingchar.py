def missing_char(str, n):
  left = str[:n]
  right = str[n + 1:]
  new_string = left + right
  return new_string    