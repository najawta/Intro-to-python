def add(a, b, c):
    res = a + b + c
    return res


def addition(*nums):
    """Returns the sum of all the numbers passed as arguments
    Parameters:
    integers or floats or a mix of integers and floats
    Returns:
    Integers or floats
    """
    total=sum(nums)
    return total

addition(8, 5)

def build_profile(**kwargs): #dict key-word args
    for k, w in kwargs.items():
        print(f"{k}:{w}")

def fancy_function(name, *nums, **kwargs):
    print(name)
    print(nums)
    print(kwargs)

# anonymous ==lambda
# def square(num):
#     return num*num
#
# result =square(s)
# print(result)

square = lambda num: num*num
print(square(5))
res=square(2.9)
print(res)

surface_area_cylinder= lambda r, h : 22/7 *r**2*2+22/7*2*r*h

print(surface_area_cylinder(14,20))

people=[
    {"name":"Alex","age":30},
    {"name":"Bob","age":22},
    {"name":"Aria","age":20},
]
# lambda x:x["age"]
sorted_by_age= sorted(people,key=lambda x:x["age"], reverse=True)
print(sorted_by_age)

# build_profile(age=100, name="Jane", proffesions="programming")



# call function
# print(add(9, 7, 5))

# print(addition(8, 3, 7, 100,5))
# print(addition(8, 3))
# print(addition(8,3,6,8,9,9))