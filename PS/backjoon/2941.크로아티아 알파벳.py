S = input()

croatia = ["c=","c-","dz=","d-","lj","nj","s=","z="]

for c in croatia:
    S = S.replace(c, "C")
print(len(S))