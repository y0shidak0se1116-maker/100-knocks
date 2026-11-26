import random

s = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

s_list = s.split()

result_list = []

for i in range(len(s_list)):
    if len(s_list[i]) > 4:
        k = s_list[i]
        extract = k[1:len(k)-1]
        extract_list = list(extract)
        random.shuffle(extract_list)
        s1 = ''.join(extract_list)
        result_list.append(k[:1] + s1 + k[-1:])
    else:
        result_list.append(s_list[i])
    
result = ' '.join(result_list)
print(result)