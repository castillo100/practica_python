import re
with open("preproinsulin-seq.txt") as f:
    data = f.read()
# print(data)
# pattern = r"[A-Z/0-9\n]|\s{2,}"
pattern = r"[A-Z/0-9\n\s]"
# pattern = r"[A-Z/0-9\n\s]"

result = re.sub(pattern, "", data)
print(result)
print(len(result))
