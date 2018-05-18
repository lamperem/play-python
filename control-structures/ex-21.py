# For Loops

words = ["hello", "world", "spam", "eggs"]
counter = 0
max_index = len(words) - 1

# using while loop
while counter <= max_index:
   word = words[counter]
   print(word + "!")
   counter = counter + 1 

# using for
for word in words:
	print(word + "!")

# for with range
for i in range(5):
	print("hello python")