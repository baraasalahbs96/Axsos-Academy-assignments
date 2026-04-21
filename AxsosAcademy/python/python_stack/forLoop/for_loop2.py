# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def biggie_size(lst):
    for i in range(len(lst)):
        if lst[i] > 0:
            lst[i] = “big”
    return lst
print(biggie_size([-1, 3, 5, -5]))
# 
# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def count_positives(lst):
    count = 0
    for val in lst:
        if val > 0:
            count += 1
    lst[-1] = count
    return lst
print(count_positives([-1, 1, 1, 1]))       
print(count_positives([1, 6, -4, -2, -7, 2])) 
 
# 
# Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
def sum_total(lst):
    total = 0
    for val in lst:
        total += val
    return total
print(sum_total([1, 2, 3, 4]))   
print(sum_total([6, 3, -2])) 
# 
# Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5
def average(lst):
    total = 0
    for val in lst:
        total += val
    return total / len(lst)
print(average([1, 2, 3, 4]))
# 
# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
def my_length(lst):
    count = 0
    for _ in lst:
        count += 1
    return count
print(my_length([37, 2, 1, -9]))  
print(my_length([])) 
# 
# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
def minimum(lst):
    if len(lst) == 0:
        return False
    min_val = lst[0]
    for val in lst:
        if val < min_val:
            min_val = val
    return min_val
print(minimum([37, 2, 1, -9]))  
print(minimum([]))     
#
# Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
def maximum(lst):
    if len(lst) == 0:
        return False
    max_val = lst[0]
    for val in lst:
        if val > max_val:
            max_val = val
    return max_val
print(maximum([37, 2, 1, -9]))  
print(maximum([]))    
# 
# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimate_analysis(lst):
    return {‘sumTotal’: sum_total(lst),‘average’: average(lst),‘minimum’: minimum(lst),‘maximum’: maximum(lst),‘length’: my_length(lst)}
print(ultimate_analysis([37, 2, 1, -9]))
# 
# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverse_list(lst):
    left = 0
    right = len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst
print(reverse_list([37, 2, 1, -9]))