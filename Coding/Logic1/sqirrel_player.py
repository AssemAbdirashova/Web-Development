def squirrel_play(temp, is_summer):
  if not is_summer and (temp >= 60 and temp <= 90): return True
  if is_summer and (temp >= 60 and temp <= 100): return True
  else: return False