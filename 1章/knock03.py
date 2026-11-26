s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
result = []

w = s.split()

for i in range(len(w)):
    result.append(len(w[i].strip(",.")))

print(result)