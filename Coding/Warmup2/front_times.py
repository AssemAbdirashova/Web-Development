def front_times(str, n):
  pref = 3
  if pref > len(str):
    pref = len(str)
  front = str[:pref]
  
  ans = ""
  for i in range(n):
    ans += front
  return ans