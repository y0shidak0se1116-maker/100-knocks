def cipher(str):
    result = ""
    for i in range(len(str)):
        if str[i].islower():
            result = result + chr(219 - ord(str[i]))
        else:
            result = result + str[i]

    return result

s = "Hello World!"
t = cipher(s)
print("暗号化\n")
print(t)
print("\n")

print("復号化")
print(cipher(t))