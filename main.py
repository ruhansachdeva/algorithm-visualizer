from core import bubble, selection, linear, binary
from guardrails import is_sorted
def get_list():
    nums = []
    while True:
        choose_num = input("choose a number to add to your list: ")
        if choose_num == "end":
            return nums
        nums.append(int(choose_num))


while True:
    what_to_vis = input("what would you like to visualise (search/sort) ('end' to stop) ").lower()
    if what_to_vis == "end":
        break
    elif what_to_vis == "search":
        nums = get_list()
        choose_targ = int(input("choose a target to search for "))

        which_search = input("which search algorithm would you like to visualize (binary/linear) ").lower()
        if which_search == "binary":
            if not is_sorted(nums):
                print("Binary needs to be sorted to run! ")
                continue
            is_found = binary(nums, choose_targ) != -1
            

        elif which_search == "linear":
            is_found = linear(nums, choose_targ) != -1

        if not is_found:
            print("target was not found in the list! ")
            continue
    elif what_to_vis == "sort":
        nums = get_list()
        which_sort = input("which sorting algorithm would you like to visualize (bubble/selection) ").lower()
        if which_sort == "bubble":
            bubble(nums)
        elif which_sort == "selection":
            selection(nums)