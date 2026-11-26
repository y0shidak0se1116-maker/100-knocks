def ngram(str,n):
    result = []

    for i in range(len(str)-n+1):
        result.append(str[i:i+n])

    return result

s1 = "paraparaparadise"
s2 = "paragraph"

x = ngram(s1,2)
y = ngram(s2,2)

result1 = set(x) | set(y)
result2 = set(x) & set(y)
result3 = set(x) - set(y)

print("和集合\n")
print(result1)
print("\n")

print("積集合\n")
print(result2)
print("\n")

print("差集合\n")
print(result3)
print("\n")

if("se" in x):
    print("se はXに含まれる")
else:
    print("se はXに含まれない")

if("se" in y):
    print("se はYに含まれる")
else:
    print("se はYに含まれない")