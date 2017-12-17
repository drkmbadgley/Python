def convert(string):
    try:
        return float(string)

    except ValueError:
        print("could not convert string to float!")

c = convert("3.1415926")
print(c)

d = convert("taco.tuesday")
print(d)
