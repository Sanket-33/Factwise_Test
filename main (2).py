#Question 1
def removeDuplicates(nums):
    j = 1
    i = 0
    while j<len(nums):
      if nums[i]!=nums[j]:
          nums[i+1],nums[j]=nums[j],nums[i+1]
          i+=1
      j+=1
nums = [0,0,1,1,1,2,2,3,3,4]
removeDuplicates(nums)
print(nums)