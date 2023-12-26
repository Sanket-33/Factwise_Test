#Question 4
def binarySearch(nums,target):
  low,high = 0,len(nums)-1
  index = 0
  while low<=high:
    mid = low + (high-low)//2
    if nums[mid] == target:
      index = mid
      break
    elif nums[mid]<target:
      index = mid+1
      low = mid+1
    else:
      index = mid-1
      high= mid -1
  return index
nums =[1,3,5,6]
binarySearch(nums,5)