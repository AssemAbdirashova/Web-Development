def max_end3(nums):

 list = []
 if nums[0] > nums[2]: max = nums[0]
 if nums[0] < nums[2]: max = nums[2]
 if nums[0] == nums[2]: max = nums[0]
 
 list.append(max)
 list.append(max)
 list.append(max)
 return list