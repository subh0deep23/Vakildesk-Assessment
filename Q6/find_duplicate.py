def findDuplicate(nums):
    # Phase 1: Detect the cycle
    slow = nums[0]
    fast = nums[0]
    
    # Move slow by one step and fast by two steps
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Phase 2: Find the entrance to the cycle
    slow = nums[0]  # reset slow to the start
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow

# Example usage:
nums = [1, 3, 4, 2, 2]
print(findDuplicate(nums))  # Output: 2
