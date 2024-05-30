def performselectionsort(nums):
    n=len(nums)
    fixThisIndex=n-1
    while fixThisIndex >0:
        maxEleIndex = fixThisIndex

        for index in range(fixThisIndex):
            if nums[index] > nums[maxEleIndex]:
                maxEleIndex=index
        if maxEleIndex !=fixThisIndex:
            temp=nums[maxEleIndex]
            nums[maxEleIndex]=nums[fixThisIndex]
            nums[fixThisIndex]=temp
        print(nums)
        fixThisIndex -=1
nums=[56,12,26,14,8,31]
performselectionsort(nums)
