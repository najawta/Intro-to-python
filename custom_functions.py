def greet():
    print("Hello")
    # greet()


def greeting(name):
    print(f"Hello {name}")


def volume_cylinder(radius, height):
    v = 22 / 7 * radius ** 2 * height
    print(round(v,2))


def volume_cylinder_better(radius, height):
    v = 22 / 7 * radius ** 2 * height
    return v


def volume_surface(radius, height):
    v = 22 / 7 * radius ** 2 * height
    a = 22 / 7 * radius ** 2 * 2 + 22 / 7 * radius ** 2 * height
    return v, a


# volume_cylinder(10,20)
# volume_cylinder(8,18)

# greet()
greeting("Sila")
greeting("Samia")
greeting("Ahmed")

result = volume_cylinder_better(6.5, 8.9)
print(round(result, 3))

with open("volumes.txt", "w") as file:
    file.write(str(result))

volume, area = volume_surface(10, 20)
print(f"volume is {volume} and area is {area}")

# named parameters
v, a =volume_surface(height=20, radius=10)
print(f"volume is {v} and area is {a}")

def divide(a=1,b=1,  should_round=False):
    res =a/b
    if should_round==True:
        return round(res,2)
    else:
        return res


print(divide(9,5.11,True))
print(divide(4,8 ))


