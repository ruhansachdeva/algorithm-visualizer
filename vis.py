# hypothetical search algorithm visualization function
# render the full array we're doing search on, the target, and the current number we're looking at
def vis_search(arr, target, curr_index):
    # [ 1, 2, 3 ]
    #      ^
    # target: 3

    for i in range(len(arr)):
        num = str(arr[i])
        if i == curr_index:
            num += "<"

        print(num)
    print(f"target: {target}")
    print("----------------------------------------")

def vis_sort(arr, curr_index, compare_index):
    for i in range(len(arr)):
        nums = str(arr[i])
        if i == curr_index or i == compare_index:
            nums += "<"
        print(nums)
    print("----------------------------------------")