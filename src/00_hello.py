# Print "Hello, world!" to your terminal

name = "Darren"
line = "Hello " + name
print(line)

# list
lst = [1, 4, 10, 10, "cat", 10, 23]

# add an element at the end
lst.append(3.5)
lst.append([100, 200, 300])
lst.insert(2, 'hello')
# only removes the first element from the left that matches the value
lst.remove(10)
# lst.remove(103)  # does not exist therefore semantic error/ run time error
print(lst)

# [6, 'a', 2.5]                  # List - ordered values
# ('foo', 'bar', 3)              # Tuple - *immutable* ordered values
# {2, 17}                        # Set - collection of distinct values
# {'a': 'Awesome', 'b': 'Best'}  # Dictionary - key, value pairs

# for item in lst:
#     print(item)

# for i in range(6):
#     print(lst[i])

# Dictionary is a list but has key value pairs
dic = {"foo": 12, "bar": 34}
print(dic)
val = dic["foo"]
print(val)

# format string also aka f string
print(f'garbage {val}')

num = 1010.256

print(f'value {num}')
