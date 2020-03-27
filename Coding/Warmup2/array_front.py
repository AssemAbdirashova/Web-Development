def array_front9(nums):
  last = len(nums)
  if last > 4:
    last = 4
  
  for i in range(last):
    if nums[i] == 9:
      return True
  return False