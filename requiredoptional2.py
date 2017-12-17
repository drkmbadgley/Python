a = input("type length:")
b = input("type width:")
c = input("type height:")

a = int(a)
b = int(b)
c = int(c)

def house(a, b, c, color="blue", local="rural"):
    return a*b*c, color, local

result = house(a,b,c)
print(result)
