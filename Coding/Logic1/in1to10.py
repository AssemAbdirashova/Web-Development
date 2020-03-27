def in1to10(n, outside_mode):
  if not outside_mode and (n >= 1 and n <= 10): return True
  if outside_mode and (n <= 1 or n >= 10): return True
  else: return False