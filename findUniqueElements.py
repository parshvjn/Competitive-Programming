d = []
e = [1,4,1,2,3,4]
for item in e:
    if item in d:
        continue
    else:
        d.append(item)

print(d)

print(set(e))