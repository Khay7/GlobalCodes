# numbers = [34.6,-203.4,44.9,68.3,-12.2,44.6,12.7]
numbers = [12,54,33,67,24,89,11,24,47]
words = ("hello","my","name","is","Sam")

# def even_numbers(n):
#     if(n % 2 == 0):
#         return n


# even_numbers_filter = list(filter(even_numbers,numbers))
# print(even_numbers_filter)

# even_numbers_map = list(map(even_numbers,numbers))
# print(even_numbers_map)



# even_numbers_lambda = list(map((lambda n: n % 2 == 0),numbers))
# print (even_numbers_lambda) 


# def positve_numbers(n):
#  return n
# positve_numbers = [num for num in numbers if num > 0]
# print(positve_numbers)

def even_numbers(n):
 return n
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)


uppercase_lenghts = [(word.upper(), len(word)) for word in words]
print(uppercase_lenghts)

 

def join_strings(words):
   return join_strings(words) 
   
words = ["hello","my","lover"]
helloworld = join_strings(words)
print(helloworld)
