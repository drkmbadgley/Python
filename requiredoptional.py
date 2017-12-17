a = input("type length:")
b = input("type width:")
c = input("type height:")
color = input("color:")
local = input("Is it city, suburb, or rural:")

a = int(a)
b = int(b)
c = int(c)

def house(a, b, c, color="blue", local="rural"):
    return a*b*c, color, local

result = house(a,b,c)
print(result)
print(result, red, city)
