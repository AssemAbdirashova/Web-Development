def string_match(a, b):
  minimum = min(len(a), len(b))
  cnt = 0
  for i in range(minimum-1):
    sub1 = a[i:i+2]
    sub2 = b[i:i+2]
    if sub1 == sub2:
      cnt += 1
  return cnt