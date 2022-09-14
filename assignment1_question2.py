def reverse(s):
    str = ""

    for i in s :
        str = i + str
    return str

s = "Edyoda"

print("original string:",end="")
print(s)

print("mirrored string:",end="")
print(reverse(s))