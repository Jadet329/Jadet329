x = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")
x = x.replace("-", " ")
x = x.strip()
x = x.lower()
if x == "42":
    print("Yes")
elif x == "forty two":
    print("Yes")
else:
    print("No")
