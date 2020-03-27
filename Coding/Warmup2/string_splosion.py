def string_splosion(str):
  ans = ""
  for i in range(len(str)):
    ans += str[:i+1]
  return ans