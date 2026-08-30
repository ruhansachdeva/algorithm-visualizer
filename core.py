from vis import vis_sort, vis_search

# Search

def binary(nums, targ):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (right + left) // 2
        vis_search(nums, targ, mid)
        if targ < nums[mid]:
            right = mid - 1
        elif targ > nums[mid]:
            left = mid + 1
        else:
            return mid
    return -1


def linear(nums, targ):
    for i in range(len(nums)):
        vis_search(nums, targ, i)
        if nums[i] == targ:
            return i
    return -1

# Sort

def bubble(nums):
    for i in range(len(nums)):
  
        for j in range(len(nums) - 1):
            vis_sort(nums, j, j + 1)
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
    return nums

def selection(nums):
    for i in range(len(nums) - 1):
        cur_smallest = i
        for j in range(i, len(nums)):
            vis_sort(nums, i, j)
            if nums[j] < nums[cur_smallest]:
                cur_smallest = j

        temp = nums[cur_smallest]
        nums[cur_smallest] = nums[i]
        nums[i] = temp
    return nums