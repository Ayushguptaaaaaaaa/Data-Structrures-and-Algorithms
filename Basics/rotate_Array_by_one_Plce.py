def rotate_array(nums, direction,n):
    if direction == "right":
        temp=nums[n-1]
        for i in range(n-2,-1,-1):
            nums[i+1]=nums[i]

        nums[0]=temp
        return nums
    
    elif direction == "left":
        temp=nums[0]
        for i in range(1,n):
            nums[i-1]=nums[i]

        nums[n-1]=temp
        return nums






nums=[]
n=int(input("Enter the number of elements in the array: "))
for i in range(n):
    nums.append(int(input("Enter the element: ")) )

print("The original array is:", nums)

direction=input("Enter the direction to rotate the array (left/right): ")

print("The array after rotating it by one place is:",rotate_array(nums, direction, n))


# Another way to rotate the array by one place is to use slicing. Here is an example of how to do it:
# nums[:]=nums[:-1]+nums[0:n-1]
# nums[:]=nums[n-1]+nums[0:n-1]

