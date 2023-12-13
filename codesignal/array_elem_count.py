"""
Given an array of integers a, your task is to calculate the digits that occur the most number of times in the array. 
Return the array of these digits in ascending order.

Example

For a = [25, 2, 3, 57, 38, 41], the output should be solution(a) = [2, 3, 5].

Here are the number of times each digit appears in the array:

0 -> 0
1 -> 1
2 -> 2
3 -> 2
4 -> 1
5 -> 2
6 -> 0
7 -> 1
8 -> 1
The most number of times any number occurs in the array is 2, and the digits which appear 2 times are 2, 3 and 5. So the answer is [2, 3, 5].
"""

def Solution(a):
    arr_to_string = "".join([str(i) for i in a])
    
    hashmap = {}
    for elem in arr_to_string:
        if elem in hashmap:
            hashmap[elem] += 1
        else:
            hashmap[elem] = 1
    
    max_elem = 0
    for elem in hashmap.values():
        max_elem = max(max_elem, elem)
    
    print(max_elem)
    
    return_arr = []
    
    for elem in hashmap:
        if hashmap[elem] == max_elem:
            return_arr.append(int(elem))
            
    return sorted(return_arr)
    
    
print(Solution([25, 2, 3, 57, 38, 41]))