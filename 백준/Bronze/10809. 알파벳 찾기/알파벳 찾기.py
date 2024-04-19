S = input()
li = [sp for sp in S]

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
witch = []

for i in alphabet:
    if i in li:
        witch.append(li.index(i))
    else:
        witch.append(-1)

print(" ".join(map(str,witch)))