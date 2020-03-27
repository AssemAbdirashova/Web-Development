def sum2(nums):
  sum = 0
  if len(nums) >= 2:
    sum = nums[0] + nums[1]
  if len(nums) == 1:
    sum = nums[0]
  if len(nums) < 1:
    sum = 0
  return sum