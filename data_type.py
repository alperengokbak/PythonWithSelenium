''' There are 8 types data in Python. We can display them group by group;
1-) Text Type: str(String)
2-) Numeric Types: int(Integer), float, complex
3-) Sequence Types: list, tuple, range
4-) Mapping Type: dict
5-) Set Type: set, frozenset
6-) Boolean Type: bool
7-) None Type: NoneType

As an extra, give example for conditionals statments. That's why, we can visit the;
https://www.kodlama.io website. For example:
1-) Scoring area is conditional statment's example
2-) Permissions, each users cannot have same permission. We take advantage from conditional.
3-) Category of the courses.
'''
# Now, lets give example some of them;

# Text Type
text = "Country"
print(f"{text} is {type(text)}")

# Numeric Types
num1 = 25
print(f"{num1} is {type(num1)}")

num2 = 25.18
print(f"{num2} is {type(num2)}")

num3 = 25 + 18j
print(f"{num3} is {type(num3)}")

# Sequence Types
my_list = list() # Python provide to add different data type inside of list().
my_list.append(18)
my_list.append("Country")
my_list.append(("Miami", "California"))
print(f"{my_list} is {type(my_list)}")

my_tuple = ("Euro", "Dollar", 99)
print(f"{my_tuple} is {type(my_tuple)}")

# Mapping Type
my_dict = dict()
my_dict["Miami"] = "Usa"
my_dict["Berlin"] = "Germany"
print(f"{my_dict} is {type(my_dict)}")

# Set Type
my_set = set()
my_set.add(18)
my_set.add(18) # We can add same value, but it's not going to be displayed to terminal.
my_set.add("Stockholm")
print(f"{my_set} is {type(my_set)}")

my_set2 = frozenset(my_set) # The frozenset() function returns an immutable frozenset object initialized with elements from the given iterable.
print(f"{my_set2} is {type(my_set2)}")

# Bool Type
my_bool = True
if my_bool:
    print("We completed the whole data types!!!")
else:
    print("Lets continue another task...")
