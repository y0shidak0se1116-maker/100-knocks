def ngram(str,n):
    result = []

    for i in range(len(str)-n+1):
        result.append(str[i:i+n])

    return result

s = "I am an NLPer"

a = ngram(s,3)
b = ngram(s.split(),2)

print("文字tri-gram\n")
print(a)
print("\n")

print("単語bi-gram\n")
print(b)
print("\n")