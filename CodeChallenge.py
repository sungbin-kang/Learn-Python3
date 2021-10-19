import random

# Write your function here
def combine_sort(lst1, lst2):
    new_list = lst1.copy().append(lst2)
    # new_list.sort()
    return new_list


# Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

nums = range(1, 13)
print(nums)

numbers_b = random.sample(range(1000), 12)
print(numbers_b)