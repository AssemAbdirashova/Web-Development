def centered_average(nums):
  sum = 0
  new_list = nums
  new_list.remove(max(nums))
  new_list.remove(min(nums))
  for i in new_list:
    sum += i
  return sum/len(new_list)