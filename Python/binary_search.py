# binary search using recursion
# array is assumed to be sorted
def binary_search(arr, low, high, x):

	if high >= low:

		mid = (high + low)//2  #finding the middle element using floor division
		if arr[mid] == x: #if the element to be searched is the middle element
			return mid
		    
		elif arr[mid] > x: #if less than middle element, search the left sub-array 
			return binary_search(arr, low, mid - 1, x)

		else: #if greater than middle element, search the right sub-array
			return binary_search(arr, mid + 1, high, x)

	else: #not found
		return -1

arr = [ 2, 3, 4, 10, 40 ]
x = 10

result = binary_search(arr, 0, len(arr)-1, x) #function call

if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")
