# List Functions

# add element to list in last position
nums = [1,2,3]
nums.append(4)
print(nums)

# get the numbers of items in list
size = len(nums)
print(size)

# add element to list in wherever position
index = 2
nums.insert(index,6)
print(nums)

# find the first occurrence of element in list
letters = ['a','b','a','c','d','b']
print(letters.index('b'))

# Item with the maximum or minimum value
nums1 = [1,2,3,5,4,0]
print( max(nums1) )
print( min(nums1) )

# Number repeat of item in list
print( letters.count('b') )

# Remove element in list
letters.remove(letters[4])
print ( letters )

# Reverses elements in list
letters.reverse()
print( letters )

