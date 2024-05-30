def performbubblesort(nums):
    n=len(nums)
    fixThisIndex = n-1

    while fixThisIndex >0:
        for index in range(fixThisIndex):
            if nums[index]>nums[index+1]:
                temp=nums[index]
                nums[index]=nums[index+1]
                nums[index+1]=temp
        print(nums)
        fixThisIndex -=1
nums=[10,8,3,16,13,7]
print("before sorting :",nums)
performbubblesort(nums)
print("After sorting:",nums)
