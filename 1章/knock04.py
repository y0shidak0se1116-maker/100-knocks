s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

w = s.split()
k = []
result = {}


for i in range(len(w)):
    if i == 0 or i == 4 or i == 5 or i == 6 or i == 7 or i == 8 or i == 14 or i == 15 or i == 18:
        k = w[i]
        result[k[:1]] = (i + 1)
    else:
        k = w[i]
        result[k[:2]] = (i + 1)

print(result)