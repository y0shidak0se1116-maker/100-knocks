a = "パトカー"
b = "タクシー"
s = ""

a_list = list(a)
b_list = list(b)

for i in range(4):
    s = s + a_list[i] + b_list[i]

print(s)