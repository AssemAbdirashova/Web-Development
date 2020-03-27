def cigar_party(cigars, is_weekend):
  if is_weekend and cigars >= 40 and cigars <= 60:
    return True
  if not is_weekend and cigars >= 40 and cigars <= 60: return True
  if is_weekend and cigars > 60: return True
  else: return False