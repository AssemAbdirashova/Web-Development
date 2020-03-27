def array_count9(nums):
  cnt = 0 
  for num in nums:
    if num == 9:
      cnt += 1
  return cnt