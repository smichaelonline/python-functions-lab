# 1. Write a function named `sum_to` that accepts a single integer, `n`, and returns the sum of the integers from 1 to `n`.

#* For example:
  # sum_to(6)  # returns 21
  # sum_to(10) # returns 55

def sum_to(num): #call function
  sum = 0 #assign starting sum to 0
  for n in range(1, num + 1): 
  #use range to loop a specific number of times to add from 1 to entered number
    sum += n 
  return sum 

# print(sum_to(6)) # return 21
# print(sum_to(20))# return 210 


#------------------------------

#2. Write a function named `largest` that takes a list of numbers as an argument and returns the largest number in that list.
    
#* For example:
  # largest([1, 2, 3, 4, 0])  # returns 4
  # largest([10, 4, 2, 231, 91, 54])  # returns 231

def largest(nums): #define function and place nums in parameters 
  largest = 0 # set largest to 0 
  for num in nums: # for loop to look at each number within list of numbers 
    if num > largest: # if statement to assign largest num in list to largest 
      largest = num 
  return largest #return largest number 

# print(largest([7, 10, 12, 15])) # return 15 


#------------------------------

#3. Write a function named occurrences that takes two string arguments as input and counts the number of occurrences of the second string inside the first string.

#* For example: 
  # occurrences('fleep floop', 'e')   # returns 2
  # occurrences('fleep floop', 'p')   # returns 2
  # occurrences('fleep floop', 'ee')  # returns 1
  # occurrences('fleep floop', 'fe')  # returns 0

def occurences(int_string, string2): 
  return int_string.count(string2) # count method returns the numbers of times the string2 value is present in the initial string (int_string)

print(occurences('soupso', 'so'))

#! need to rename parameters so they make more sense 

#------------------------------

#4. Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product. HINT: Review your notes on args.

#* For example: 
  # product(-1, 4) # returns -4
  # product(2, 5, 5) # returns 50
  # product(4, 0.5, 5) # returns 10.0