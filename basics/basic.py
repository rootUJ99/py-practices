# data types in python 

print("fundamental -> int, bool, float")
basic_int = 200
basic_bool = False
basic_float = 2.2
print(basic_int, basic_bool, basic_float)

print("sequences -> list, string, tuples")
basic_list = ["abc", 10, None]
basic_tuple =  ("abc", 10, None)
basic_stirng = "this is a basic string with \n"
print(basic_list, basic_stirng, basic_tuple)

print("sequences -> empty tuple and one value tupel")
empty_basic_tuple = tuple() # use tuple function for declaring empty tuple
one_value_tuple = (10,) # use comma else it is considered as value inside of a parenthesis
print(empty_basic_tuple, one_value_tuple)

print("sequence -> applicable operators")
appliable_operators_on_string = "this is plain string and i can do anything with it"
print("og string ->", appliable_operators_on_string)
print("slice with start, and end ->", appliable_operators_on_string[0:10])
print("slice with start, end and step ->", appliable_operators_on_string[0:10:2])

operator_on_string1 = "abc"
operator_on_string2 = "pqr"
operator_on_string3 = "abc"
operator_on_list1 = ["abc", "pqr"]
operator_on_list2 = ["pqr", "abc"]
operator_on_tuple1 = ("abc", "pqr")
operator_on_tuple2 = ("abc", "pqr")
operator_on_tuple3 = operator_on_tuple1
print("with + operator", operator_on_string1 + operator_on_string2)
print("with * operator", operator_on_string1 * 2) # any one value has to be a number
print("containment check ->", "with" in appliable_operators_on_string)
print("containment check ->", "with" not in appliable_operators_on_string)
print("euqal to", operator_on_string1 == operator_on_string3)
print("not euqal to", operator_on_string1 != operator_on_string3)
print("less than on list", operator_on_list1 < operator_on_list2)
print("is operator", operator_on_tuple1 is operator_on_tuple3) # is operator is being used to check if both are same refrences
operator_on_list1 += operator_on_list2
print("extending a list with +=", operator_on_list1)
operator_on_tuple1 += operator_on_tuple2
print("extending a tuple with +=", operator_on_tuple1)
operator_on_list3 = operator_on_list1
operator_on_list3.append("yooo")
print(operator_on_list1, operator_on_list3, "are they same still")

print("sets and dicts in python")
first_set = {1, 2, 3}
second_set = set()
third_set = {1, 2, 3}
fourth_set = {1, 2, 3, 4}


print(first_set, type(second_set))
print("comaprison on set ->", first_set == third_set)
print("grater on set ->", first_set >= second_set)
print("union on set ->", first_set | fourth_set)
print("intersection on set ->", first_set & fourth_set)
print("contains on first ->",  fourth_set - first_set)
print("contains in one of the set ->",  first_set ^ fourth_set)

first_dict = {"first":1, "second":2, "third":3}
second_dict = {}
third_dict = {"first":1, "second":2, "third":3}
print(first_dict, type(second_dict))
print("comparison on dict ->", first_dict == third_dict)
print("comparison on dict ->", first_dict != second_dict)

# condition statement
value = "Loss"
if (value == "Profit"):
    print("yes it is profit")
elif (value == "Loss"):
    print("Nooo it is a loss")
else:
    print("Please provide right value")


# looping
counter = 0
while(counter <= 5):
    print(counter)
    counter += 1

looping_list = ["one", "two", "three"]
print("normal looping")
for i in range(10):
    print(i)

print("looping in reverse")
for i in range(9, -1, -1):
    print(i)

print("looping in list")
for i in looping_list:
    print(i)

print("looping with list index")
for index, ele in enumerate(looping_list):
    print("index", index, "element",ele)


print("looping with list with else loop")
for index, ele in enumerate(looping_list):
    print(index)
else:
    print("end of the block")

print("looping with list with else loop it will not work if it loop breaks")
for index, ele in enumerate(looping_list):
    if index == 2:
        print(index)
else:
    print("end of the block")


try:
    a = int("")
except (TypeError, ValueError) as e:
    # raise TypeError("please provide int as argument", e) # use this for throwing the error
     print(TypeError("please provide int as argument", e))
except:
    print("can not conver to a int")


def test_function(name, country="india"):
    return name, country

def test_function2(name, country="india"):
    name = "test func2 " + name
    return name, country

print(test_function("ujwal", "uk"))
print(test_function("ujwal", country="us"))
test_func_name, test_func_country = test_function("ujwal")
print(test_func_country, test_func_name)

test_func_name2 = "sri"
test_func2_res = test_function2(test_func_name2)
print(test_func_name2, test_func2_res)
